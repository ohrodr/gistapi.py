class Gists(object):
    """Gist API wrapper"""

    def __init__(self, username=None, token=None):
        # Token-based Authentication is unnecessary, gist api still in alpha
        self._username = username
        self._token = token

    @staticmethod
    def fetch_by_user(name):
        """Return a list of public Gist objects owned by
        the given GitHub username."""

        _url = GIST_JSON % 'gists/%s' % name

        # Return a list of Gist objects
        return [Gist(json=g)
                for g in json.loads(requests.get(_url).content)['gists']]

