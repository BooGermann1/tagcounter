from Tagcounter.misc import BadResultException


class Prompter:

    def __init__(self, filepath):
        self.abbr_dict = {}
        self.parse(filepath)

    def parse(self, path):
        """As built-in YAML parser is excessive for such kind of a jobs
            Handwritten parser was made"""
        try:
            with open(path, 'r') as file:
                lines = file.readlines()
            if not lines:
                raise BadResultException("Prompt file is corrupted")
            for line in lines:
                """Parser recognizes [abbreviation] : [url] records"""
                words = line.split(':')
                if len(words) == 2:
                    self.abbr_dict[words[0].strip()] = words[1].strip()
        except FileNotFoundError:
            raise BadResultException("Prompt file is unavailable")

    def get_url(self, abbreviate):
        if abbreviate in self.abbr_dict:
            return self.abbr_dict[abbreviate]
        else:
            return

    def get_all_urls(self):
        """Get set of unique urls as values from file"""
        unique_urls = set(values for values in self.abbr_dict.values())
        return [v for v in unique_urls]