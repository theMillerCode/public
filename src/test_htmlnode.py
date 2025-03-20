import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode

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

    def test_to_html_raises_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_to_html_with_empty_value(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_none_tag(self):
        node = LeafNode(None, "Hello")
        self.assertEqual(node.to_html(), "Hello")

    def test_to_html_with_none_tag_and_empty_value(self):
        node = LeafNode(None, "")
        with self.assertRaises(ValueError):
            node.to_html()

#to test Parent
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_leaf_node_with_tag_and_value(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_node_with_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")
    
    def test_leaf_node_with_empty_value(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_node_with_none_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_node_with_props(self):
        node = LeafNode("a", "Click me", props={"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me</a>')
    
    def test_parent_node_basic(self):
        node = ParentNode("div", [LeafNode("p", "Paragraph")])
        self.assertEqual(node.to_html(), "<div><p>Paragraph</p></div>")

    def test_parent_node_with_multiple_children(self):
        node = ParentNode("ul", [
            LeafNode("li", "Item 1"),
            LeafNode("li", "Item 2"),
            LeafNode("li", "Item 3")
        ])
        self.assertEqual(node.to_html(), "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>")

def test_parent_node_with_no_tag(self):
    with self.assertRaises(ValueError):
        ParentNode(None, [LeafNode("p", "Test")]).to_html()

def test_parent_node_with_no_children(self):
    with self.assertRaises(ValueError):
        ParentNode("div", None).to_html()

def test_parent_node_with_empty_children_list(self):
    node = ParentNode("div", [])
    self.assertEqual(node.to_html(), "<div></div>")

def test_nested_parent_nodes(self):
    grandchild = LeafNode("span", "I'm deep")
    child = ParentNode("div", [grandchild])
    parent = ParentNode("section", [child])
    self.assertEqual(parent.to_html(), "<section><div><span>I'm deep</span></div></section>")

def test_mixed_leaf_and_parent_children(self):

    node = ParentNode("div", [
        LeafNode("h1", "Title"),
        ParentNode("p", [
            LeafNode("b", "Bold"),
            LeafNode(None, " and "),
            LeafNode("i", "italic")
        ]),
        LeafNode(None, "Plain text")
    ])
    self.assertEqual(node.to_html(), 
                    "<div><h1>Title</h1><p><b>Bold</b> and <i>italic</i></p>Plain text</div>")

if __name__ == '__main__':
    unittest.main()