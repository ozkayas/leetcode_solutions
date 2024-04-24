class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Yanit uzerinde binary search yapma mantigi var. Yanit kumesi
        # Bu tip sorularda bir yardimci metot var genelde
         
        def daysForCapacity(capacity: int) -> int:
            total = 0
            days = 0

            for w in weights:
                total += w
                if total == capacity:
                    #found the last of a package
                    days += 1
                    total = 0
                elif total > capacity:
                    # prev index was the last of a package
                    days += 1
                    total = w

            if total > 0: days += 1  
            return days

        l = max(weights)
        r = sum(weights)

        while l <= r:
            m = (l+r)//2
            # We will try to minimize the m
            # capacity inc -> days decrease
            d = daysForCapacity(m)
            if d <= days: #We are ok or maybe still can decrease capacity
                r = m - 1
            else:
                l = m + 1
            # print("l,r,m", l,r,m)
        
        return l






'''        # [1,2,3,4,5,6,7,8,9,10]
                              ^
                   d = 4
                   total = 10
        # 10 - sumof array arasi binary search?

'''