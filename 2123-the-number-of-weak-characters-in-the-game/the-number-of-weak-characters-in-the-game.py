class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        ## Bucket Sort algo
        ans = 0
        bucket = defaultdict(list)
        # Need these for looping reverse
        min_atk, max_atk = float("inf"), float("-inf")

        for at,de in properties:
            # Update min, max
            min_atk = min(min_atk, at)
            max_atk = max(max_atk, at)
            bucket[at].append(de)
        
        # Holds the max defense of the previous bucket/group that has higher attack than this bucket
        max_prev_def = float("-inf")

        for i in range(max_atk, min_atk-1, -1):
            if not bucket[i]:
                continue
            
            for defense in bucket[i]:
                if defense < max_prev_def:
                    ans += 1
                
            # wait for the loop to finish then update maxPrevDef
            max_prev_def = max( max_prev_def, max(bucket[i]))

        return ans
        