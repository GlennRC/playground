import sys
import math

def solve(grades):
    # Complete this function
    res = []
    for i in range(1,len(grades)):
        if grades[i] < 40:
            res.append(str(grades[i])) 
            continue

        g_r = math.ceil(float(grades[i])/5.0)*5

        if g_r - grades[i] < 3:
            res.append(str(g_r))
        else:
            res.append(str(grades[i])) 
    return res

def main():
    result = solve([4,73,67,38,33])
    print("\n".join(result))

if __name__ == "__main__":
    main()