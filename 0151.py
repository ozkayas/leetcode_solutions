# Input: s = "the sky is blue"
# Output: "blue is sky the"


def reverseWords(s: str) -> str:
    res = []
    i, j, n = 0,0,len(s)
    while(i<n):
        # loop until finding a character,
        while(i<n and s[i] == " "):
            i +=1
        if i == n: break
        j = i+1 # set j pointer to the next position

        while(j<n and s[j] != " "):
            j +=1
  
        foundWord = s[i:j]
        i = j

        res.append(foundWord)
    res.reverse()
    # print(res)
    # i = j

    print(" ".join(res))
    return " ".join(res)







s = "the sky is blue"
reverseWords(s)


