class Site:
    pass

class Blogger(Site):
    def __init__(self, user):
        self.user = user

    def get_links(self, posts):
        print(len(posts))  # This won't get printed in the test.
        return posts
