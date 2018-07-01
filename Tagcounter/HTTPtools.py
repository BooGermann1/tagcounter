import http.client
from urllib.parse import urlparse, urlunparse, ParseResult
from Tagcounter.misc import BadResultException


def http_request(url):
    parsed_url = urlparse(url_preparse(url))
    try:
        if parsed_url.scheme == 'https' or parsed_url.scheme == '':
            connection = http.client.HTTPSConnection(parsed_url.netloc)
        elif parsed_url.scheme == 'http':
            connection = http.client.HTTPConnection(parsed_url.netloc)
        """Make just a path without schemes and domains"""
        path = urlunparse(ParseResult('', '', parsed_url.path, parsed_url.params, \
                                      parsed_url.query, parsed_url.fragment))
    except ValueError:
        raise BadResultException("Requested URL is invalid")

    try:
        connection.request('GET', path)
        response = connection.getresponse()
        return response.read()
    except:
        raise BadResultException("Requested URL is not available")


def url_preparse(url):
    """Define a scheme (HTTP or HTTPS)"""
    if url.startswith('http://') or url.startswith('https://'):
        return url
    else:
        return 'https://'+url
