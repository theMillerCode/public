import re
import unittest
from regex_fun import *

class TestMarkdownExtractors(unittest.TestCase):

    def test_extract_markdown_images_basic(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_no_match(self):
        text = "This text has no images."
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_single_match(self):
        text = "Just one image: ![single image](http://example.com/single.jpg)"
        expected = [("single image", "http://example.com/single.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links_basic(self):
        text = "Here's a [link](https://www.example.com) and another [link2](http://test.org)."
        expected = [("link", "https://www.example.com"), ("link2", "http://test.org")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_image_and_link(self):
        text = "This text has ![image](http://image.com) and a [link](http://link.com)."
        expected = [("link", "http://link.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_no_match(self):
        text = "This text has no links or images."
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_single_match(self):
        text = "Just one link: [single link](http://single.com)"
        expected = [("single link", "http://single.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_nested_brackets(self):
        text = "here is a [text with [inner brackets]](http://test.com)"
        expected = [("text with [inner brackets]", "http://test.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_images_nested_brackets(self):
         text = "here is an ![image with [inner brackets]](http://test.com)"
         expected = [("image with [inner brackets]", "http://test.com")]
         self.assertEqual(extract_markdown_images(text), expected)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)