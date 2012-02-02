import unittest
import meeplib

# note:
#
# functions start within test_ are discovered and run
#       between setUp and tearDown;
# setUp and tearDown are run *once* for *each* test_ function.

class TestMeepLib(unittest.TestCase):
    def setUp(self):
        u = meeplib.User('foo', 'bar')
        v = meeplib.User('foo2', 'bar2')
        m = meeplib.Message('the title', 'the content', u)

    def test_for_message_existence(self):
        x = meeplib.get_all_threads()[0]
        y = x.get_all_posts()
        assert len(y) == 1
        assert x.title == 'the title'
        assert y[0].post == 'the content'

    def test_message_ownership(self):
        x = meeplib.get_all_users()
        assert len(x) == 2
        u = x[0]

        t = meeplib.get_all_threads()[0]
        x = t.get_all_posts()
        assert len(x) == 1
        m = x[0]

        assert m.author == u

    def test_get_next_user_id(self):
        x = meeplib._get_next_user_id()
        assert type(x) == int
    def test_search(self):
        x = meeplib.search_message_dict("content")
        assert len(x) == 1

    def tearDown(self):
        t = meeplib.get_all_threads()[0]
        m = t.get_all_posts()[0]
        t.delete_post(m)

        u = meeplib.get_all_users()[0]
       
        v = meeplib.get_all_users()[1]
        meeplib.delete_user(u)
        meeplib.delete_user(v)

        assert len(meeplib._threads) == 0
        assert len(meeplib._users) == 0
        assert len(meeplib._user_ids) == 0

if __name__ == '__main__':
    unittest.main()
