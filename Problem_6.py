class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union_and_intersection(llist_big,llist_small):
    llist_union=LinkedList()                                        # List to add union elements
    llist_intersection=LinkedList()                                 # List to add intersection elements
    list_dict=dict()                                                # Dictionary to keep track of elements added to above lists
    node=llist_big.head
    while node:
        llist_union.append(node)                                    # Add all the elements of bigger list to union list
        list_dict[node.value]=list_dict.get(node.value,0)+1
        node=node.next

    node=llist_small.head

    while node:
        if node.value in list_dict and list_dict[node.value]>0:
            llist_intersection.append(node)                         # Add elements which are common to both lists
        else:
            llist_union.append(node)                                # Add elemts which are unique to smaller list as common elements have been already added
        node=node.next

    return llist_union,llist_intersection

def union(llist_1, llist_2):
    # Since total run time will be O(n) where n- number of elements of bigger list, hence call the function accordingly
    if llist_1.size()>llist_2.size():
        ans=union_and_intersection(llist_1,llist_2)
    else:
        ans=union_and_intersection(llist_2,llist_1)
    return ans[0]

def intersection(llist_1, llist_2):
    # Since total run time will be O(n) where n- number of elements of bigger list, hence call the function accordingly
    if llist_1.size()>llist_2.size():
        ans=union_and_intersection(llist_1,llist_2)
    else:
        ans=union_and_intersection(llist_2,llist_1)
    return ans[1]


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
