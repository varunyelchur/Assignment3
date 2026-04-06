# Assignment3

Varun Yelchur
73222847

Run using the .in files in the data and you can compare it with the corresponding .out file
Example: python3 src/code.py < data/test1.in

Conditions for testing:
- Input is same format as the assignment which can be seen in the .in files
- In the string, each character needs a value attached to it
- Strings are greater than length of 25

1. For the graph below, I made a graph using the time it took for all the tests to run and give an output. From the graph you can see that the times are pretty much very similar with just the first time being a little higher which could be due to it being the first test run. Input sizes are over 25 but still similar to each other and they range from 0.017 to 0.028 seconds.



2. 
First, OPT(i,j) is the maximum value of a common subsequence
Then, Initialize a table for OPT
Base Cases:
- OPT(i, 0) = 0
- OPT(0, j) = 0
Recurrence:
if A[i] == B[j]:
OPT(i, j) = max(
    OPT(i-1, j-1)+ val[A[i]],
    OPT(i-1, j),
    OPT(i, j-1)
)
else:
OPT(i, j) = max(
    OPT(i-1, j),
    OPT(i, j-1)
)

For every i and j:
If the characters match,
- we use the match and add its value
AND also store the value when we ignore and keep the result fromm before
The value that provides the larger one out of those two is the one we choose

If they don't match,
- we skip a character from string A AND store the value when we skip a character from string B
The value that provides the larger one out of those two is the one we choose

This is correct because at each step we are considering every possible choice and taking the best value. The base cases are 0 because an empty string has no common subsequence.


3. 
First, OPT(i,j) is the length of the HVLCS
Then, Initialize a table for OPT
Base Cases:
- OPT(i, 0) = 0
- OPT(0, j) = 0

'''function(A, B, val):
    n is len(A)
    m is len(B)
    create dp[0..n][0..m], fill it all with zeros
    for i from 1 to n:
        for j from 1 to m:
            if A[i] equals B[j]:
                dp[i][j] = dp[i-1][j-1] +val[A[i]]
                dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    i = n
    j = m
    length = 0
    while i is greater than 0 and j is greater than 0:
        if A[i] equals B[j] and dp[i][j] equals dp[i-1][j-1] + val[A[i]]:
            length = length + 1
            i = i-1 
            j = j-1
        else if dp[i-1][j] >= dp[i][j-1]:
            i = i-1
        else:
            j = j-1
    return length'''

Once the table is filled, the overall runtime is O(nm). This is because we fill the table size which is n by m and each cell is O(1). The traceback is also O(n+m) so it results in O(n*m).

