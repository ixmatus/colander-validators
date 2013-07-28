import re


def email(value):
    """Validate an email address
    
    >>> email("barney@purpledino.com")
    True
    >>> email("barneydino.com")
    'An email address must contain a single @'
    """

    usernameRE = re.compile(r"^[^ \t\n\r@<>()]+$", re.I)
    domainRE = re.compile(r'''
        ^(?:[a-z0-9][a-z0-9\-]{0,62}\.)+ # (sub)domain - alpha followed by 62max chars (63 total)
        [a-z]{2,}$                       # TLD
    ''', re.I | re.VERBOSE)

    messages = dict(
        empty='Please enter an email address',
        noAt='An email address must contain a single @',
        badUsername='The username portion of the email address is invalid'
                    ' (the portion before the @: {username!s}',
        socketError='An error occured when trying to connect to the server:'
                    ' {error!s}',
        badDomain='The domain portion of the email address is invalid'
                  ' (the portion after the @: {domain!s}',
        domainDoesNotExist='The domain of the email address does not exist'
                           ' (the portion after the @: {domain!s}')

    if not value:
        return messages['empty']

    value = value.strip()
    splitted = value.split('@', 1)

    try:
        username, domain=splitted
    except ValueError:
        return messages['noAt']

    if not usernameRE.search(username):
        return messages['badUsername'].format(username=username)

    if not domainRE.search(domain):
        return messages['badDomain'].format(domain=domain)

    return True


def url(value):
    """Validate a URL completely

    >>> url("ixmat.us")
    True
    >>> url("ixmat")
    'You must provide a full domain name (like ixmat.com)'

    """

    messages = dict(
        noScheme='You must start your URL with http://, https://, etc',
        badURL='That is not a valid URL',
        httpError='An error occurred when trying to access the URL: {error!s}',
        socketError='An error occured when trying to connect to the server: {error!s}',
        notFound='The server responded that the page could not be found',
        status='The server responded with a bad status code ({status!s})',
        noTLD='You must provide a full domain name (like {domain!s}.com)')

    url_re = re.compile(r'''
        ^(http|https)://
        (?:[%:\w]*@)?                              # authenticator
        (?:                                        # ip or domain
        (?P<ip>(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))|
        (?P<domain>[a-z0-9][a-z0-9\-]{,62}\.)*     # subdomain
        (?P<tld>[a-z]{2,63}|xn--[a-z0-9\-]{2,59})  # top level domain
        )
        (?::[0-9]{1,5})?                           # port
        # files/delims/etc
        (?P<path>/[a-z0-9\-\._~:/\?#\[\]@!%\$&\'\(\)\*\+,;=]*)?
        $
    ''', re.I | re.VERBOSE)

    scheme_re = re.compile(r'^[a-zA-Z]+:')

    value = value.strip()

    if not scheme_re.search(value):
        value = "http://" + value

    value = encode_idna(value)
    match = scheme_re.search(value)

    if not match:
        return messages['noScheme']

    value = match.group(0).lower() + value[len(match.group(0)):]
    match = url_re.search(value)

    if not match:
        return messages['badURL']

    if not match.group('domain'):
        return messages['noTLD'].format(domain=match.group('tld'))

    return True


def encode_idna(value):
    from urllib.parse import urlparse, urlunparse
    scheme, netloc, path, params, query, fragment = urlparse(value)
    try:
        netloc = netloc.encode('idna')
        netloc = netloc.decode('ascii')
        return str(urlunparse((scheme,
                                        netloc,
                                        path,
                                        params,
                                        query,
                                        fragment)))
    except UnicodeError:
        return value
