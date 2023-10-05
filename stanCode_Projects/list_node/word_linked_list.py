"""
File: word_linked_list.py
Name: Jessica
----------------------------
This program demonstrates constructing
a character-based linked list from the word
input by user.
"""


class ListNode:
    def __init__(self, data, pointer):
        self.val = data
        self.next = pointer


def main():
    word = input('Word: ')
    linked_list = None
    end = None
    for ch in word:
        new_node = ListNode(ch, None)
        if linked_list is None:
            # First Data
            linked_list = new_node
            end = new_node
        else:
            end.next = new_node
            end = end.next
    traversal(linked_list)


def traversal(linked_list):
    cur = linked_list
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


if __name__ == '__main__':
    main()
