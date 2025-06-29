from unittest import TestCase
from section3lena.bloglena import Bloglena

class BloglenaTest(TestCase):

    def test_create_blog(self):
        b = Bloglena('TestName', 'TestContent', [])

        self.assertEqual(b.title, 'TestName')
        self.assertEqual(b.author, 'TestContent')
        self.assertListEqual(b.posts, [])

