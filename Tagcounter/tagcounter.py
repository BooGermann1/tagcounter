import sys
from Tagcounter.dao import DAO
from Tagcounter.CLI import CLI
from Tagcounter.GUI import GUI
from Tagcounter.prompter import Prompter
from Tagcounter.misc import BadResultException, TagMethod, LOG_LOCATION, PROMPT_LOCATION
from Tagcounter.tagparser import get_tags_list
from Tagcounter.logger import log

class Controller:

    """Class with all specific business logic"""

    def __init__(self, ui=None, storage=None, prm=None):
        self.ui = ui
        self.dao = storage
        self.prompt = prm
        """Provide controller's reference to chosen UI"""
        ui.set_controller(self)


    def process_url(self, url, method=TagMethod.GET):
        """Process every url request (http/db)"""

        url_syn = ""
        """Try to find an url by the given synonym"""
        try:
            url_syn = self.prompt.get_url(url)
        except BadResultException as e:
            self.ui.print_msg(e.get_public_message())
        except Exception:
            pass

        url_to_proc = url_syn if url_syn else url

        if not url or url.isspace():
            """If given url is empty"""
            self.ui.print_msg("Please specify valid URL")
            return

        if method == TagMethod.GET:
            try:
                parsed_dict = get_tags_list(url_to_proc)
            except BadResultException as e:
                self.ui.print_msg(e.get_public_message())
            else:
                """All successful http requests shall be logged and saved in db """
                log(LOG_LOCATION, url_to_proc)
                self.dao.save(url_to_proc, parsed_dict)
                self.ui.print_tags(self.dict_to_str(parsed_dict))

        elif method == TagMethod.VIEW:
            try:
                restored_dict = self.dao.read(url_to_proc)
            except BadResultException as e:
                self.ui.print_msg(e.get_public_message())
            else:
                self.ui.print_tags(self.dict_to_str(restored_dict))

    @staticmethod
    def dict_to_str(tags_dict):
        """String presentation for tags dictionary to convenient output"""
        str_dict = ''
        for k, v in tags_dict.items():
            str_dict += '{} : {}\n'.format(k, v)
        return str_dict

    def get_urls_from_file(self):
        """Return all unique urls we have in prompt file"""
        if self.prompt:
            return self.prompt.get_all_urls()


def print_wrong_usage():
    print("Please run script without arguments for GUI"
          " or use two arguments --get or --view and required url for console version.")


def make_app_with_ui(ui):
    """Controller constructor for different UIs"""
    storage = None
    hlp = None
    try:
        storage = DAO()
        hlp = Prompter(PROMPT_LOCATION)
    except BadResultException as e:
        print(e.get_public_message())
    return Controller(ui, storage, hlp)

def main():
    args = sys.argv
    if len(args) == 3:
        """Command line interface shall be run if 2 arguments are given"""
        cli = CLI()
        app = make_app_with_ui(cli)
        cli.run(args)
    elif len(args) == 1:
        """GUI shall be used in case if no arguments were given"""
        gui = GUI()
        app = make_app_with_ui(gui)
        gui.run()
    else:
        print_wrong_usage()

if __name__ == '__main__':
    main()