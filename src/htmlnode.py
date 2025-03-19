class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value #A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children #A list of HTMLNode objects representing the children of this node
        self.props = props #A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}


    def to_html(self):
        raise NotImplementedError("add error message?")
    
    def props_to_html(self):
        final_string = ""
        if self.props == None:
            return ""
        else:
            for key, value in self.props.items():
                final_string += f" {key}=\"{value}\""
            return final_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        pass

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value

    def to_html(self):
        
        if self.value == None or self.value == "":
            raise ValueError("value cannot be empty")
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):

        if self.tag == None:
            raise ValueError("tag node req")
        if self.children == None:
            raise ValueError("children node req")
        
        # Convert props to HTML attributes
        props_html = self.props_to_html()

        # Recursively call to_html on each child and concatenate their results
        children_html = ''.join(child.to_html() for child in self.children)
        
        # Combine the opening tag with attributes, the children HTML, and the closing tag
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"

