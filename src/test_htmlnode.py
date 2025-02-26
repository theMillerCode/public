import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # Create a node with some props
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank"
            }
        )
        # Check if the output matches expected string
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )
    def test_init_default(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_tag(self):
        node = HTMLNode(tag='p')
        self.assertEqual(node.tag, 'p')
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_value(self):
        node = HTMLNode(value='Hello, World!')
        self.assertIsNone(node.tag)
        self.assertEqual(node.value, 'Hello, World!')
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_children(self):
        child_node = HTMLNode(tag='a')
        node = HTMLNode(children=[child_node])
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [child_node])
        self.assertIsNone(node.props)

    def test_init_with_props(self):
        node = HTMLNode(props={'href': 'https://www.google.com'})
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertEqual(node.props, {'href': 'https://www.google.com'})

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_non_empty(self):
        node = HTMLNode(props={'href': 'https://www.google.com', 'class': 'btn'})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" class="btn"')

    def test_repr(self):
        node = HTMLNode(tag='p', value='Hello', children=None, props={'class': 'text'})
        expected_repr = "HTMLNode(p, Hello, None, {'class': 'text'})"
        self.assertEqual(repr(node), expected_repr)

    def test_repr_empty(self):
        node = HTMLNode()
        expected_repr = "HTMLNode(None, None, None, None)"
        self.assertEqual(repr(node), expected_repr)

    def test_repr_with_children(self):
        child_node = HTMLNode(tag='a')
        node = HTMLNode(tag='div', children=[child_node])
        expected_repr = "HTMLNode(div, None, [HTMLNode(a, None, None, None)], None)"
        self.assertEqual(repr(node), expected_repr)

    def test_to_html_raises_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == '__main__':
    unittest.main()