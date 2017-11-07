from linked_list import LinkedList
from linked_list import ListNode
from list_generator import ListGenerator
import heapq

def heapsort(iterable:list):
    if iterable == None:
        raise Exception("Iterable is None")

    h = []
    for item in iterable:
        heapq.heappush(h, item)
    return [heapq.heappop(h) for _ in range(len(h))]

def linkToList(node:ListNode):
    if node == None:
        raise Exception("node is None")

    l = []
    curr = node
    while curr:
        l.append(curr.val)
        curr = curr.next
    return l

def print_link_list(node):
    if node == None:
        raise Exception("node is None")

    curr = node
    while curr:
        print("{} ".format(curr.val), end="")
        curr = curr.next
    print()
            

def main():
    listGen = ListGenerator()
    lists = []

    num_lists = 10
    rand_low = 0
    rand_high = 100
    list_size = 20

    sortedLists = listGen.sortedLists(num_lists,rand_low,rand_high,list_size)
    
    nodes = []
    for l in sortedLists:
        node = LinkedList(l.tolist()).head
        nodes.append(node)

    lists = [linkToList(n) for n in nodes]
    print(lists)

    lists = heapsort(lists)

    print(lists)

    ml = []
    for item in lists:
        ml.extend(item)

    print(ml)





if __name__ == "__main__":
    main()

            

        

