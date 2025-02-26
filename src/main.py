from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    # Test different node types
    text_node = TextNode("Hello, world!", TextType.TEXT, None)
    bold_node = TextNode("Bold text", TextType.BOLD, None)
    link_node = TextNode("Click me", TextType.LINK, "https://www.boot.dev")
    
    # Print them to test your __repr__ method
    print(text_node)
    print(bold_node)
    print(link_node)

    #Test different htmlnode types
    html_node = HTMLNode("p")

    # Print them to test your __repr__ method
    print(html_node)

    
    # Test equality
    node1 = TextNode("Same text", TextType.TEXT, None)
    node2 = TextNode("Same text", TextType.TEXT, None)
    node3 = TextNode("Different text", TextType.TEXT, None)
    
    print(node1 == node2)  # Should print True
    print(node1 == node3)  # Should print False

if __name__ == "__main__":
    main()