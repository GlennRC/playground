import numpy as np

class ListGenerator(object):
    def sortedLists(self, num, low, high, size):
        lists = []
        offset = 0
        for _ in range(num):  
            lists.append(np.arange(offset, size+offset))
            offset = np.random.randint(low, high)
        np.random.shuffle(lists)
        return lists
    
    def unsortedLists(self, num, low, high, size):
        lists = []
        size = np.random.randint(low, high)
        for _ in range(num):
            lists.append(np.random.random_integers(low,high,size))
        np.random.shuffle(lists)
        return lists
