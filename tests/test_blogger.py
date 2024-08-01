import pytest
import myapplication as tum

class TestBlogger:
    @classmethod
    def setup_class(self):
        self.user = "alice"
        self.b = tum.Blogger(self.user)
        print("Execução do primeiro teste da pipeline!")

    def test_inherit(self):
        assert issubclass(tum.Blogger, tum.Site)
        posts = ["post1", "post2", "post3", "post4"]
        links = self.b.get_links(posts)
        print(len(links))  

    def test_get_links_length(self):  
        print("Execução do segundo teste da pipeline!")
        posts = ["post_a", "post_b"]
        links = self.b.get_links(posts)
        assert len(links) == 2  