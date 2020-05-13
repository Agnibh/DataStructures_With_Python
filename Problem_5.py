import hashlib

def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

class LinkedList:
    # Linked List class to point to the head and tail of the block chain. New blocks are added to the tail
    def __init__(self,block):
        self.block=block
        self.next=None

class BlockChain:

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def add_block(self,timestamp,data,previous_hash):
        if previous_hash==0:                                                # If the block chain is empty
            self.tail=LinkedList(Block(timestamp,data,0))
            self.head=self.tail
            self.size=1
            return
        if self.tail.hash==previous_hash:                                    # Add new block to tail if previous hash of new block matches tail's hash
            self.tail.next=LinkedList(Block(timestamp,data,previous_hash))
            self.tail=self.tail.next
            self.size+=1
            return
        return
