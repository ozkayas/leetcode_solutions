class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freqShort = Counter(nums1)
        freqLong = Counter(nums2)

        if len(nums1) > len(nums2):
            freqShort, freqLong = freqLong, freqShort

        ans = []

        for k, v in freqShort.items():
            if k in freqLong:
                commonFreq = min(v, freqLong[k])
                for i in range(commonFreq):
                    ans.append(k)

        return ans 

