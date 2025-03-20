import unittest

from textnode import TextNode, TextType
from convert_txt_2_html import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node7 = TextNode("Same text", TextType.TEXT, None)
        node9 = TextNode("Different text", TextType.TEXT, None)
        self.assertNotEqual(node7, node9)
    
    def test_not_eq_type(self):
        node17 = TextNode("Same text", TextType.BOLD, None)
        node19 = TextNode("Same text", TextType.TEXT, None)
        self.assertNotEqual(node17, node19)

    def test_eq_url(self):
        node27 = TextNode("Same text", TextType.BOLD, None)
        node29 = TextNode("Same text", TextType.BOLD)
        self.assertEqual(node27, node29)

    def test_eq_url_02(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node37 = TextNode("Same text", TextType.BOLD, None)
        node39 = TextNode("Same text", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node37, node39)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev", "alt": "This is an image"})

if __name__ == "__main__":
    unittest.main()