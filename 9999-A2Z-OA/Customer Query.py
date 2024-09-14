### Burada neredeyse aynisi var Leetcodeda
# https://leetcode.com/problems/search-suggestions-system/solutions/864637/python-3-two-methods-sort-trie-explanation/
from typing import List

from bisect import bisect, bisect_left

### Once bunu deneyerek basla
def suggestedProducts(A: List[str], searchWord: str) -> List[List[str]]:
    A = [w.lower() for w in A]
    searchWord = searchWord.lower()

    A.sort()
    res = []
    for i in range(1, len(searchWord)):
        cur = customer_query[:i + 1].lower()
        i = bisect_left(A, cur)
        res.append([w for w in A[i:i+3] if w.startswith(cur)])

    return res

# Example usage:
repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
customer_query = "mouse"
print(suggestedProducts(repository, customer_query))  # [["mobile", "moneypot", "mouse"], ["mouse", "mousepad"], ["mouse", "mousepad"]]

def customerQuery(repository, customerQuery):

    repository_2=[]
    Res =[]
    repository = sorted([x.lower() for x in repository] )
    N = len(customerQuery)
    if N <2:
        return " "

    k =2
    while k <= N:
        for suggest in repository:

            if k <= len(suggest) and customerQuery[:k] in suggest[:k]:
                repository_2.append(suggest)

        repository = repository_2
        m = min(3, len(repository))
        Res.append(repository[:m])
        repository_2 =[]

        k+=1
    return Res


print(customerQuery(["mobile","mouse","moneypot","monitor","mousepad"], "mouse")) #[["mobile","mouse","moneypot"],["mouse","mousepad"],["mouse","mousepad"]]


## BAska bir cozum
def search_suggestions(repository, customer_query):
    res = []

    # Iterate through each prefix length
    for i in range(1, len(customer_query)):
        s = customer_query[:i + 1].lower()  # Take the prefix of length i+1
        temp = []

        # Check each word in the repository if it starts with the prefix
        for word in repository:
            if word.lower().startswith(s):
                temp.append(word.lower())

        # Sort the temporary list lexicographically
        temp.sort()

        # Take the first 3 elements from the sorted list
        res.append(temp[:3])

    return res


# Example usage:
repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
customer_query = "mouse"
print(search_suggestions(repository, customer_query))  # [["mobile", "moneypot", "mouse"], ["mouse", "mousepad"], ["mouse", "mousepad"]]


