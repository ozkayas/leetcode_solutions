def checkSimilarPasswords(newPasswords, oldPasswords):
    # Initialize return object of the list of string
    ans = []

    n = len(newPasswords)

    # Iterate over all the password to check the similarity
    for k in range(n):
        #Take a new password
        newPass = newPasswords[k]
        #Take a old password
        oldPass = oldPasswords[k]

        #Two iterator i and j will point towards the index of both the strings
        i = 0
        j = 0
        while i < len(newPass) and j < len(oldPass):
            #Get a character from new password
            newPassChar = newPass[i]

            #Get a character from old password
            oldPassChar = oldPass[j]

            #Calculate shifted new password
            newPassShiftedOldChar = 'a'
            if newPassChar == 'z':
                newPassShiftedOldChar = 'a'
            else:
                newPassShiftedOldChar = chr(ord(newPassChar) + 1)

            #if either newPassChar or newPassShiftedOldChar matches with oldPassCharwe will search for next oldPassChar
            if oldPassChar == newPassChar or oldPassChar == newPassShiftedOldChar:
                j = j + 1
            i = i + 1

        #if we get all the matches for oldPass then yes
        if j == len(oldPass):
            ans.append("YES")
        #if we do not find all the matches for oldPass then no
        else:
            ans.append("NO")

    return ans


#These are user input for checking you can change them as per your requirements
newPasswords = ["aaccbbee", "aab"]
oldPasswords = ["bdbf", "aee"]

print(checkSimilarPasswords(newPasswords, oldPasswords))
print(checkSimilarPasswords(["baacbab", "accdb", "baacba"], ["abdbc", "ach", "abb"])) # ["YES", "NO", "YES"]
