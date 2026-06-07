from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown: str) -> BlockType:
    md_lines = markdown.split("\n")
    if markdown.startswith("#"):
        is_proper_heading = True
        num_hashtags = 0
        for i in range(len(markdown)):
            if markdown[i] == "#":
                num_hashtags += 1
                if num_hashtags > 6:
                    is_proper_heading = False
                    break
            if markdown[i] == " ":
                break
        if is_proper_heading:
            return BlockType.HEADING
    if markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE
    is_quote = True
    for line in md_lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE
    is_unordered_list = True
    for line in md_lines:
        if not line.startswith("- "):
            is_unordered_list = False
            break
    if is_unordered_list:
        return BlockType.UNORDERED_LIST
    is_ordered_list = True
    for i in range(0, len(md_lines)):
        if not md_lines[i].startswith(f"{i + 1}. "):
            is_ordered_list = False
            break
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
