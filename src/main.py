from textnode import TextNode, TextType
from htmlnode import *
from fuctions import *

def main():
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    test = split_nodes_image([node])
    print(test)
main()