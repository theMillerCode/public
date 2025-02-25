import unittest

from textnode import TextNode, TextType


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

    def test_not_eq_url(self):
        node37 = TextNode("Same text", TextType.BOLD, None)
        node39 = TextNode("Same text", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node37, node39)

    

if __name__ == "__main__":
    unittest.main()