# Huffman_encoding_decoding
This is Huffman encoding and decoding algorithm built in python.

Short description:
A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.
The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many different types of pseudocode for this tree, but at its basic core, 3 things have to be made:
1. Build a huffman tree
2. Encode the given data
3. Decode the data, with the encoded data and tree as an input

This is my pseudocode for following project:
- Take a string and determine the relevant frequencies of the characters
- Build and sort a list of tuples from lowest to highest frequencies
- Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters
- Trim the Huffman Tree (remove the frequencies from the previously built tree)
- Encode the text into its compressed form
- Decode the text from its compressed form
- You then will need to create encoding, decoding, and sizing schemas

Note: In the repository I've got 6 files:
- Node_class, tree_class and queue_class serve as helper classes here
- Huffman_encoding_and_decoding is the core of the project here, where tree is built and data encoded and decoded
- In test_function I've provided some test cases to get a better grasph of what the entire program does
- Further explanation is provided in code_explanation.txt

# Creator
Tjaž Eržen
- LinkedIn: https://www.linkedin.com/in/tjaz-erzen-688aa1190/
- Github: https://github.com/tjazerzen

# Further research
Here's a few resources to get deeper understanding of this compression algorithm:
- Visualization of building the tree: https://people.ok.ubc.ca/ylucet/DS/Huffman.html
- Additional explanation: https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
