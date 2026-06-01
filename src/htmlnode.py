class HTMLNode:
    def __init__(
        self,
        tag: "str | None" = None,
        value: "str | None" = None,
        children: list["HTMLNode"] | None = None,
        props: "dict | None" = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if not self.props:
            return ""

        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'

        return result

    def __repr__(self) -> str:
        return f"HTMLNode: tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: "str | None",
        children: list["HTMLNode"] | None,
        props: "dict | None" = None,
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag")
        if not self.children:
            raise ValueError("Missing children nodes")
        representation = f"<{self.tag + self.props_to_html()}>"
        for child in self.children:
            representation += child.to_html()
        return representation + f"</{self.tag}>"


class LeafNode(HTMLNode):
    def __init__(
        self, tag: "str | None", value: "str", props: "dict | None" = None
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("Missing value")
        if not self.tag:
            return self.value
        return f"<{self.tag + self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode: tag={self.tag}, value={self.value}, props={self.props}"
