from node_class import Node
from tree_class import Tree

"""
Pseudocode:
1. Take a string and determine the relevant frequencies of the characters
2. Build and sort a list of tuples from lowest to highest frequencies
3. Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters
4. Trim the Huffman Tree (remove the frequencies from the previously built tree)
5. Encode the text into its compressed form
"""

def return_frequency(data):
    # Take a string and determine the relevant frequencies of the characters
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    lst = [(v, k) for k, v in frequency.items()]
    # Build and sort a list of tuples from lowest to highest frequencies
    lst.sort(reverse=True)
    return lst


# A helper function to the build_tree()
def sort_values(nodes_list, node):
    node_value, char1 = node.value
    index = 0
    max_index = len(nodes_list)
    while True:
        if index == max_index:
            nodes_list.append(node)
            return
        current_val, char2 = nodes_list[index].value
        if current_val <= node_value:
            nodes_list.insert(index, node)
            return
        index += 1


# Build a Huffman Tree: nodes are stored in list with their values (frequencies) in descending order.
# Two nodes with the lowest frequencies form a tree node. That node gets pushed back into the list and the process repeats
def build_tree(data):
    lst = return_frequency(data)
    nodes_list = []
    for node_value in lst:
        node = Node(node_value)
        nodes_list.append(node)

    while len(nodes_list) != 1:
        first_node = nodes_list.pop()
        second_node = nodes_list.pop()
        val1, char1 = first_node.value
        val2, char2 = second_node.value
        node = Node((val1 + val2, char1 + char2))
        node.set_left_child(second_node)
        node.set_right_child(first_node)
        sort_values(nodes_list, node)

    root = nodes_list[0]
    tree = Tree()
    tree.root = root
    return tree

# the function traverses over the huffman tree and returns a dictionary with letter as keys and binary value and value.
# function get_codes() is for encoding purposes
def get_codes(root):
    if root is None:
        return {}
    frequency, characters = root.value
    char_dict = dict([(i, '') for i in list(characters)])

    left_branch = get_codes(root.get_left_child())

    for key, value in left_branch.items():
        char_dict[key] += '0' + left_branch[key]

    right_branch = get_codes(root.get_right_child())

    for key, value in right_branch.items():
        char_dict[key] += '1' + right_branch[key]

    return char_dict


# when we've got the dictionary of binary values and huffman tree, tree encoding is simple
def huffman_encoding_func(data):
    if data == '':
        return None, ''
    tree = build_tree(data)
    dict = get_codes(tree.root)
    codes = ''
    for char in data:
        codes += dict[char]
    return tree, codes


# The function traverses over the encoded data and checks if a certain piece of binary code could actually be a letter
def huffman_decoding_func(data, tree):
    if data == '':
        return ''
    dict = get_codes(tree.root)
    reversed_dict = {}
    for value, key in dict.items():
        reversed_dict[key] = value
    start_index = 0
    end_index = 1
    max_index = len(data)
    s = ''

    while start_index != max_index:
        if data[start_index : end_index] in reversed_dict:
            s += reversed_dict[data[start_index : end_index]]
            start_index = end_index
        end_index += 1

    return s




