class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = defaultdict(int)
        max_len = 0
        most_freq_char = 0

        for r in range(len(s)):
            # At each iteration recalculate window len, and freq of chars
            w_len = (r-l+1)
            freq[s[r]] += 1
            most_freq_char = max(most_freq_char, freq[s[r]])
            swappable_chars_count = w_len - most_freq_char
            # print(freq.items())

            if swappable_chars_count > k: # Not a valid substring, can not form a AAAAA, so shrink window
                freq[s[l]] -= 1
                l += 1
                w_len -= 1

            max_len = max(max_len, w_len)

        # print(l,r,freq.items(),max_len)
        return max_len



        