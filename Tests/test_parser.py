from Tagcounter.tagparser import get_tags_list
from unittest.mock import patch

html_EC0 = ("<head></head><html><p>some</p><p>text</p></html>", {"head": 1, "p": 2, "html": 1})


@patch('Tagcounter.tagparser.http_request', return_value=html_EC0[0])
def test_count_tags(TestCase):
    """Test checks whether html parser returns correctly parsed data
        HTTP client was mocked"""
    for k, v in html_EC0[1].items():
        assert get_tags_list("")[k] == v
