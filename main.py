from transformations import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    deck_path = sys.argv[1]


    text = get_deck_text(deck_path)
    lines = split_into_lines(text)
    x_del = x_delete(lines)
    tab_removed = tab_split(x_del)
    type_deleted = type_delete(tab_removed)
    shortened = collector_shorten(type_deleted)
    rearranged = rearrange(shortened)
    res = merge(rearranged)
    
    
    print(res)


def get_deck_text(path):
    with open(path) as f:
        return f.read()


    




main()