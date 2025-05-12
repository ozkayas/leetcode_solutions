class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # bucket sort algo
        bucket = defaultdict(list)
        max_at, min_at = 0, float('inf')
        for a,d in properties:
            bucket[a].append(d)
            max_at = max(max_at, a)
            min_at = min(min_at, a)

        # Reverse loop from the max_at to min_at, however skip max_at, no player in this bucket is weak
        max_def_prev = max(bucket[max_at]) # max def of the previous bucket players
        result = 0
        
        for at in range(max_at-1, min_at-1, -1):
            if not bucket[at]: continue

            max_def_cur = 0
            for defense in bucket[at]:
                max_def_cur = max(max_def_cur, defense)
                if defense < max_def_prev:
                    result += 1
            # Re-assign max_def_prev before jumping tot he next bucket
            max_def_prev = max(max_def_prev, max_def_cur)

        return result