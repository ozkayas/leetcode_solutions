class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        output = []

        for i in range(len(searchWord)):
            target = searchWord[:i+1]
            idx = bisect_left(products, target)
            subset = []
            for j in range(idx,idx+3):
                if j < len(products) and target == products[j][:i+1] :
                    subset.append(products[j])
            output.append(subset)

        return output