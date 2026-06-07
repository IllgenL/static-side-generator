import unittest

from block_markdown import markdown_to_blocks, markdown_to_html_node
from blocktype import BlockType, block_to_block_type


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_newlines(self):
        md = """
This is a test paragraph


This is another paragraph with too much newlines before it"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a test paragraph",
                "This is another paragraph with too much newlines before it",
            ],
        )

    def test_empty_blocks(self):
        md = """
This is a test paragraph




This is another paragraph with an empty paragraph before it"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a test paragraph",
                "This is another paragraph with an empty paragraph before it",
            ],
        )

    def test_heading(self):
        md = """
# This is a H1

## This is a H2

### This is a H3

#### This is a H4

##### This is a H5

###### This is a H6

####### This is no heading"""
        blocks = markdown_to_blocks(md)
        block_types = [block_to_block_type(block) for block in blocks]
        self.assertEqual(
            block_types,
            [
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.PARAGRAPH,
            ],
        )

    def test_code_block(self):
        md = """
```
This is a block of code
It is very cody```

```This is no block of code because it's missing a newline```
"""
        blocks = markdown_to_blocks(md)
        block_types = [block_to_block_type(block) for block in blocks]
        self.assertEqual(
            block_types,
            [
                BlockType.CODE,
                BlockType.PARAGRAPH,
            ],
        )

    def test_quote(self):
        md = """
> This is a quote
> Abe Lincoln said once
> Not to trust everything on the internet

> This is not quote
Since it's missing a > sign at the start of the line
"""
        blocks = markdown_to_blocks(md)
        block_types = [block_to_block_type(block) for block in blocks]
        self.assertEqual(
            block_types,
            [
                BlockType.QUOTE,
                BlockType.PARAGRAPH,
            ],
        )

    def test_unordered_list(self):
        md = """
- This is a list
- With items

- This is a list item
-This is no list item
- This is another list item"""
        blocks = markdown_to_blocks(md)
        block_types = [block_to_block_type(block) for block in blocks]
        self.assertEqual(
            block_types,
            [
                BlockType.UNORDERED_LIST,
                BlockType.PARAGRAPH,
            ],
        )

    def test_ordered_list(self):
        md = """
1. This is an ordered list
2. With multiple items

1. This is an ordered list
2.This is not item

2. This list starts at the wrong index
"""
        blocks = markdown_to_blocks(md)
        block_types = [block_to_block_type(block) for block in blocks]
        self.assertEqual(
            block_types,
            [
                BlockType.ORDERED_LIST,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
            ],
        )

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()
