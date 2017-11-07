
class Solution:
    def isMatch(s, p):
        import re
        pattern = re.compile(p)
        m = pattern.match(s)
        if m and m.group() == s:
            return True
        else:
            return False

def main():
    print(Solution.isMatch("aaa","aa"))

if __name__ == "__main__":
    main()