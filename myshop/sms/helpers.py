from requests.exceptions import RequestException, HTTPError
import sys
import requests


if sys.version_info.major == 2:
    from httplib import HTTPException
    from urllib2 import URLError
else:
    from http.client import HTTPException
    from urllib.error import URLError


NETWORK_EXCEPTIONS = (
    requests.RequestException,
    HTTPException,
    select.error,
    socket.error,
    ssl.SSLError,
    URLError,
    requests.HTTPError,
)


class ExternalError(Exception):
    pass


def post_json(url, data=None, timeout=60):

    try:
        resp = requests.post(url, data=data, timeout=5)
    except NETWORK_EXCEPTIONS as e:
        raise ExternalError('Error fetching {}, data: {}: {}'.format(url, repr(data), repr(e)))

    if resp.status_code != 200:
        raise ExternalError('Network Error: status code: {}'.format(resp.status_code))

    try:
        resp_data = resp.json()
    except (TypeError, ValueError) as e:
        raise ExternalError('Got invalid json: {}'.format(url, repr(e)))

    return resp_data
