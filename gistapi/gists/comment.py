class GistComment(object):
    """Gist comments."""

    def __init__(self):
        self.body = None
        self.created_at = None
        self.gravatar_id = None
        self.id = None
        self.updated_at = None
        self.user = None

    def __repr__(self):
        return '<gist-comment %s>' % self.id

    @staticmethod
    def from_api(jsondict):
        """Returns new instance of GistComment containing given api dict."""
        comment = GistComment()

        comment.body = jsondict.get('body', None)
        comment.created_at = datetime.strptime(jsondict.get('created_at')[:-6], '%Y/%m/%d %H:%M:%S')
        comment.gravatar_id = jsondict.get('gravatar_id', None)
        comment.id = jsondict.get('id', None)
        comment.updated_at = datetime.strptime(jsondict.get('updated_at')[:-6], '%Y/%m/%d %H:%M:%S')
        comment.user = jsondict.get('user', None)

        return comment

