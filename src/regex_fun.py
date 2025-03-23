import re

#text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

def extract_markdown_images(text):
    
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)

    #print(matches)

    return matches # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

def extract_markdown_links(text):

    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

    #print(matches)

    return matches
