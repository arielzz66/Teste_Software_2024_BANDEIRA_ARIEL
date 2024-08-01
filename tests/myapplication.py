class Site:
    pass

class Blogger(Site):
    def __init__(self, user):
        self.user = user

    def get_links(self, posts):
        print(len(posts)) 
        return posts
