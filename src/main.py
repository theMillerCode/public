from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from convert_txt_2_html import *
from split_nodes_delimiter import *


from textnode import TextNode, TextType


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    test_node = TextNode("This `is text` with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([test_node], "`", TextType.CODE)

    print(new_nodes)


main()
