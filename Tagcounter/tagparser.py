from html.parser import HTMLParser
from Tagcounter.HTTPtools import http_request


class Parser(HTMLParser):
    """Built-in HTML parser was used as simple and suitable solution"""

    def __init__(self, ):
        super().__init__()
        self.tag_dict = {}

    def parse_url(self, url):
        page = str(http_request(url))
        self.feed(page)
        """Parsing runs automatically just right after feeding"""
        return self.tag_dict

    def handle_starttag(self, tag, attrs):
        """Callback is called every finding of a tag"""
        if tag in self.tag_dict:
            self.tag_dict[tag] += 1
        else:
            self.tag_dict[tag] = 1


def get_tags_list(url):
    parser = Parser()
    return parser.parse_url(url)

