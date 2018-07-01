from Tagcounter.prompter import Prompter
import pytest
from Tagcounter.misc import BadResultException

file_EC0 = {"ynd": "yandex.ru", "yndx": "yandex.ru", "ggl": "google.com", "gog": "google.com"}


def test_no_file():
    """Test checks whether prompt module raises an exception if no file was found"""

    with pytest.raises(BadResultException):
        _ = Prompter("")


def test_all_urls(tmpdir):
    """Test checks whether prompt moduler returns all detected urls as unique set"""

    test_string = ""
    file = tmpdir.join("test_propmt.txt")
    for k, v in file_EC0.items():
        test_string += "{} : {}\n".format(k, v)
    file.write(test_string)
    helper = Prompter(file.strpath)
    all_urls = helper.get_all_urls()

    """Check whether return results are unique"""
    assert set(all_urls) == set(file_EC0.values())


def test_get_url(tmpdir):
    """Test checks whether prompt module returns url upon request with an abbreviation"""

    test_string = ""
    file = tmpdir.join("test_prompt.txt")
    for k, v in file_EC0.items():
        test_string += "{} : {}\n".format(k, v)
    file.write(test_string)
    helper = Prompter(file.strpath)
    for k, v in file_EC0.items():
        assert v == helper.get_url(k)