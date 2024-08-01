import pytest
import myapplication as tum

class TestBlogger:
    @classmethod
    def setup_class(self):
        self.user = "alice"
        self.b = tum.Blogger(self.user)
        print("This should be printed, but it won't be!")

    def test_inherit(self):
        assert issubclass(tum.Blogger, tum.Site)
        posts = ["post1", "post2", "post3"]
        links = self.b.get_links(posts)
        print(len(links))   # This won't print either.
