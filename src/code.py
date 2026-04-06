import sys

# reads input
def read():
    all = sys.stdin.readlines()
    lines = []
    for line in all:
        line = line.strip()
        if line != "":
            lines.append(line)
    num = int(lines[0])
    vals = {}
    for i in range(1, num + 1):
        chars = lines[i].split()
        x = chars[0]
        vals[x] = int(chars[1])
    a = lines[num + 1]
    b = lines[num + 2]

    return vals, a, b


#main solveing function
def solve(vals, a, b):
    lena = len(a)
    lenb = len(b)

    dp = []
    for i in range(lena+1):
        row = [0] * (lenb+1)
        dp.append(row)

    for i in range(1, lena + 1):
        for j in range(1, lenb + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + vals[a[i - 1]]
                dp[i][j] = max(dp[i][j], dp[i - 1][j],dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

      # print(dp)
    final = []
    i = lena
    j = lenb
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            if dp[i][j] == dp[i - 1][j - 1] +vals[a[i - 1]]:
                final.append(a[i - 1])
                i -= 1
                j -= 1
            else:
                i -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    final.reverse()
    answer = "".join(final)
    result = dp[lena][lenb]
    return result, answer


def main():
    vals, a, b = read()
    best, answer = solve(vals, a, b)
    print(best)
    print(answer)

if __name__ == "__main__":
    main()