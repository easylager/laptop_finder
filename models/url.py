


class AbstractUrl:

    def __init__(self, full_url):
        self.full_url = full_url

    @property
    def domen(self):
        return self.full_url.split('.')[1]

    @property
    def hash(self, is_good=True):
        if is_good:
            return self.full_url.split('/')[-1]
        return None

    def __str__(self):
        return self.full_url

    def __repr__(self):
        return self.full_url