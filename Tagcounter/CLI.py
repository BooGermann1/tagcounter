from Tagcounter.misc import TagMethod

class CLI:

    def __init__(self):
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def get_tags_from_url(self, url):
        """Get tags with a HTTP request"""
        self.controller.process_url(url, TagMethod.GET)

    def view_tags_from_url(self, url):
        """Get tags from DB"""
        self.controller.process_url(url, TagMethod.VIEW)

    def print_msg(self, message):
        print(message)

    def print_tags(self, tags):
        print('List of tags:')
        print(tags)

    def run(self, args=None):
        if len(args) == 3:
            url = args[2]
            if args[1] == '--get':
                self.get_tags_from_url(url)
            elif args[1] == '--view':
                self.view_tags_from_url(url)
            else:
                print('Please use --get or --view operation arguments')
        else:
            print('Please enter 2 arguments')
