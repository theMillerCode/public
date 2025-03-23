from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from convert_txt_2_html import *
from split_nodes_delimiter import *
from regex_fun import *

text1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
#text = "My email is lane@example.com and my friend's email is hunter@example.com"
text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

node_link = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)

node_image = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )

# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]


def main():
    #node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    #print(node)

    #test_node = TextNode("This `is text` with a `code block` word", TextType.TEXT)
    #new_nodes = split_nodes_delimiter([test_node], "`", TextType.CODE)

    split_nodes_image([node_image])

    #split_nodes_link(node_link)


main()
