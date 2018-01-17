
# def find_dup(s):
#     for i in range(len(s)):
#         for j in range(i, len(s)-1):
#             if s[i] == s[j+1]:
#                 return s[i] 
#     return None

# def is_anagram(s1, s2):
#     s3 = [l for l in s2]
#     for i in s1:
#         if i in s3:
#             s3.remove(i)
#         else:
#             print("false")
#             return
    
#     if len(s3) == 0:
#         print("true")
#     else:
#         print("false")
    
# def is_pal(s):
#     #noon
#     #civic
#     for i in range(int(len(s)/2)):
#         if s[i] != s[(len(s)-1)-i]:
#             print("no")
#             return
#     print("yes")

# def reverse_words(s):
#     s = s.split(" ")
#     return " ".join(reversed(s))

def max_diff(a):
    arr = []
    for i in range(len(a)):
        for j in range(len(a)):
            if i < j and a[i] < a[j]:
                arr.append(a[j] - a[i])
    return max(arr)


def main():
    a1 = [2,3,10,2,4,8,1]
    print(max_diff(a1))

    a2 = [6,7,9,5,6,3,2]
    print(max_diff(a2))
    

if __name__ == "__main__":
    main()
