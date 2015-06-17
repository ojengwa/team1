from main import *
import unittest


class WebTestCase(unittest.TestCase):

    
    def test_get_url(self):
        page ,title = get_page('http://google.com')
        self.assertEqual(
            'Google',
            title,
            msg='Title of Google should be'+title
        )
        self.assertEqual(
            BeautifulSoup,
            type(page),
            msg='Should return a BeautifulSoup instance'
        )

    def test_get_external(self):
        external = get_page('http://andela.co')
        self.assertNotIn(
            'andela.co',
            external,
            msg='External links should not include host domain'
        )

    



        



if __name__ == '__main__':
    unittest.main()