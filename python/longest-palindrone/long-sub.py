
def long_sub(word):
    curr = ""
    prev = ""

    for i in word:
        if i in curr:
            if len(curr) > len(prev):
                prev = (curr + ".")[:-1]
                curr = ""
        curr = curr + i
    
    if len(curr) > len(prev):
        return curr
    else:
        return prev


w = "abccdefghe"

print(long_sub(w))
