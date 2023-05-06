strA = input()
strB = input()
strT = ""

if len(strA) < len(strB):
    strT = strA
    strA = strB
    strB = strT

lenA,lenB = len(strA)+1,len(strB)+1

# Runtime Err. 긴 걸 A로 하기 <<?

lcs = [[0]*lenA for _ in range(lenB)]

for i in range(0,lenB):
    for j in range(0,lenA):
        if i == 0 or j == 0 :
            continue
        if strA[j-1] == strB[i-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(lcs[-1][-1])