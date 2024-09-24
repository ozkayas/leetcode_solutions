class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products.sort()

        for i in range(len(searchWord)):
            query = searchWord[0:i+1]
            idx = bisect_left(products,query)
            found =  []
            for j in range(idx, idx+3):
                if j < len(products) and query == products[j][0:i+1]:
                    found.append(products[j])
            ans.append(found)
        # print(ans)
        return ans



"""
"mobile",
"moneypot"
"monitor"
"mousemonitor",
"mousepad"

"""
        