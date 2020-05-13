from queue import Queue

class LinkedList:
    # Linked List to point to head and tail of priority queue
    def __init__(self,node):
        self.node=node
        self.next=next

class Node:
    # Node represents each element in the huffman tree
    def __init__(self,char,frequency):
        self.char=char
        self.freq=frequency
        self.right_child=None
        self.left_child=None

    def set_right_child(self,node):
        self.right_child=node

    def set_left_child(self,node):
        self.left_child=node

    def get_freq(self):
        return self.freq

    def get_char(self):
        return self.char

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def has_child(self):
        return self.left_child!=None

class PriorityQueue:

    def __init__(self):
        self.size=0
        self.head=None                  # Head represents the node with lowest frequency
        self.tail=None                  # Tail represents the node with highest frequency

    def add(self,node):
        # Function to add node to the priority queue
        if self.size==0:                            # If the priority queue is empty
            self.tail=LinkedList(node)
            self.head=self.tail
            self.size=1
            return

        if self.tail.node.freq<=node.freq:          # If new node has the highest frequency in the priority queue, then add it to the tail
            self.tail.next=LinkedList(node)
            self.tail=self.tail.next
            self.size+=1
            return

        if self.head.node.freq>node.freq:           # If new node has the lowest frequency in the priority queue, then add it to the head
            data=LinkedList(node)
            data.next=self.head
            self.head=data
            self.size+=1
            return

        curr_data=self.head                         # ELse traverse through the priority queue and add the new node accordingly
        prev_data=self.head
        while True:
            if curr_data.node.freq>node.freq:
                data=LinkedList(node)
                prev_data.next=data
                data.next=curr_data
                self.size+=1
                return
            prev_data=curr_data
            curr_data=curr_data.next

    def get(self):                          # Removing a node from the priority queue always take place from the head
        node=self.head.node
        self.head=self.head.next
        self.size-=1
        return node

    def len(self):
        return self.size

def huffman_encoding(data):
    char_dict=dict()                        # Dictionary to add unique characters and their frequency

    for char in data:
        char_dict[char]=char_dict.get(char,0)+1

    priority_queue=PriorityQueue()
    for char,freequency in char_dict.items():       # Initial adding of the characters to the priority queue
        node=Node(char,freequency)
        priority_queue.add(node)

    while priority_queue.len()>1:                   # Loop through the priority queue until there is a single element
        node1=priority_queue.get()                  # Get the first two nodes from the queue
        node2=priority_queue.get()
        parent_node=Node('.',node1.get_freq()+node2.get_freq())     # Create parent node whose frequency is equal to sum of child frequencies
        parent_node.set_left_child(node1)           # Set the first node as the left child
        parent_node.set_right_child(node2)          # Set the second child as the right node
        priority_queue.add(parent_node)             # Add the parent node to the priority queue

    tree=priority_queue.get()                       # Last elemnt in the queue is the root of the tree
    bit_map=create_encode_map_from_tree(tree)       # Function to map unique characters to their corresponding bit representation
    encoded_msg=generate_encode_message(data,bit_map)   # Function to generate the encoded message
    return encoded_msg,tree

def huffman_decoding(data,tree):
    bit_map=create_decode_map_from_tree(tree)       # Function to map bit representation to their corresponding unique characters
    encoded_msg=data
    decoded_msg=''
    bits=''
    for bit in encoded_msg:                         # Loop through every bit in the encoding message
        bits+=bit
        if bits in bit_map:                         # If the bits represent a character then add it to the decoded message
            decoded_msg+=bit_map[bits]
            bits=''
    return decoded_msg

def create_encode_map_from_tree(tree):
    bit_map=dict()                                  # Dictionary to map unique characters to their corresponding bit representation
    root=tree
    q=Queue()
    q.put((root,''))                                # Root node of the tree has no bit assigned to it
    while not q.empty():                            # Traverse through the tree using breadth first search algorithm
        node,bit=q.get()
        if node.has_child():
            q.put((node.get_left_child(),bit+'0'))  # Add 0 to the left node
            q.put((node.get_right_child(),bit+'1')) # Add 1 to the right node
        else:                                       # If the node has no child, then it is the leaf of the tree and represents an unique character
            bit_map[node.get_char()]=bit            # Add it to the dictionary
    return bit_map

def create_decode_map_from_tree(tree):
    bit_map=dict()                                  # Dictionary to map bit representation to their corresponding unique characters
    root=tree
    q=Queue()
    q.put((root,''))                                # Root node of the tree has no bit assigned to it
    while not q.empty():                            # Traverse through the tree using breadth first search algorithm
        node,bit=q.get()
        if node.has_child():
            q.put((node.get_left_child(),bit+'0'))  # Add 0 to the left node
            q.put((node.get_right_child(),bit+'1')) # Add 1 to the right node
        else:                                       # If the node has no child, then it is the leaf of the tree and represents an unique character
            bit_map[bit]=node.get_char()            # Add it to the dictionary
    return bit_map

def generate_encode_message(data,bit_map):          # Function to generate the encoded message
    encoded_msg=''
    for char in data:                               # Loop through each character in the original string
        encoded_msg+=bit_map[char]                  # Replace the characters to their bit representation

    return encoded_msg

import sys

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
