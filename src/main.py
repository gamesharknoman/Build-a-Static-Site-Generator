from textnode import TextNode, TextType
from htmlnode import *

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )

    node.to_html()
    print(node)
main()