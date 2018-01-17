def permute(arr, start, end):
    #base case: start = end
    if(start == end):
        print(arr)
    else:
        for i in range(start, end):
            arr[start], arr[i] = arr[i], arr[start]
            permute(arr, start+1, end)
            arr[start], arr[i] = arr[i], arr[start]

# a = ['a', 'b', 'c']

# permute(a, 0, len(a))

def is_palindrome(s):
    d = {}
    for c in s:
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
    l = [val%2 == 0 for val in d.values()]
    if len(s)%2 == 0:
        return all(l)
    else:
        return l.count(False) == 1

import random

s = "taacat"
print(is_palindrome(''.join(random.sample(s,len(s)))))





