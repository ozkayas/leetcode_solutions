'''
Question:
Sellers buy items in Walmart during sale events and sell them on Amazon to make money. You have to help a seller make maximum profit for their purchase.

You are given two lists, one for Walmart prices and another for Amazon prices of a certain item over a period of time. The ith entry in both lists represents the price of the item at the ith time in Amazon and Walmart.

Example:
Walmart: [4, 7, 5, 8]
Amazon: [6, 8, 7, 8]
Answer: 4; Seller can buy the item at 0th time index from Walmart at $4 and sell it at Amazon on the 1st time index at $8, making the profit of $4.
'''

def maxProfit(Walmart, Amazon):
    max_profit = 0
    min_walmart_price = float('inf')
    
    for i in range(len(Walmart)):
        # Find the lowest Walmart price up to the current index
        min_walmart_price = min(min_walmart_price, Walmart[i])
        # Calculate the profit by selling at the current Amazon price
        profit = Amazon[i] - min_walmart_price
        # Track the maximum profit found so far
        max_profit = max(max_profit, profit)
    
    return max_profit

# Örnek kullanım
Walmart = [4, 7, 5, 8]
Amazon = [6, 8, 7, 8]
print(maxProfit(Walmart, Amazon))  # Çıktı: 4
Walmart = [4, 7, 3, 5, 8]
Amazon = [6, 8, 7, 8, 9]
print(maxProfit(Walmart, Amazon))  # Çıktı: 4
Walmart = [3, 4, 7, 2, 8]
Amazon =  [6, 10, 8, 7, 8]
print(maxProfit(Walmart, Amazon))  # Çıktı: 4