
class LinkedList:
    #Set up class LinkedList to point to head and tail of LRU cache
    def __init__(self,value):
        self.value=value
        self.next=None

    def get_value(self):
        return self.value

class LRU_Cache(object):

    def __init__(self, capacity):
        self.LRU_dict=dict()                #Dictionary to operate get and set operation in O(1) time
        self.head=None                      # Points to the first element added
        self.tail=None                      # Points to the last element added
        self.size=0
        self.capacity=capacity

    def get(self, key):
        if key in self.LRU_dict:
            return self.LRU_dict[key]
        return -1

    def set(self, key, value):
        if self.size==0:                    # If adding the first element in the datastructure
            self.LRU_dict[key]=value
            self.tail=LinkedList(key)
            self.head=self.tail
            self.size+=1
            return

        if self.size>=self.capacity:            # If maximum capacity of the cache has reached, them remove the first element added
            key_remove=self.head.get_value()
            self.LRU_dict.pop(key_remove)
            self.head=self.head.next            # Make head point to the next element in cache which is old
            self.size-=1

        self.LRU_dict[key]=value
        self.tail.next=LinkedList(key)          # Make tail point to the newest element
        self.tail=self.tail.next
        self.size+=1
        return


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
