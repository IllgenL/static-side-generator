from textnode import TextNode, TextType


def main() -> None:
    tn = TextNode("This is some anchor text", TextType.LINK, "http://www.boot.dev")
    print(tn)


if __name__ == "__main__":
    main()
