class Solution:
    def smallestString(self, s: str) -> str:
        # Length of the input string
        length_of_string = len(s)
        # Initialize index to start from the beginning
        index = 0

        # Skip all the 'a' characters from the start
        while index < length_of_string and s[index] == "a":
            index += 1
          
        # If the string is made up entirely of 'a's, then replace the last 'a' with 'z'
        if index == length_of_string:
            return s[:-1] + "z"
          
        # Find the index where 'a' appears after the consecutive sequence of non 'a' characters
        next_a_index = index
        print(next_a_index)
        while next_a_index < length_of_string and s[next_a_index] != "a":
            next_a_index += 1
            print(next_a_index)
      
        # Decrease every character in the substring from 'index' to 'next_a_index' by one
        # and replace that part of the string with the new substring
        return (s[:index] + 
                "".join(chr(ord(char) - 1) for char in s[index:next_a_index]) +
                s[next_a_index:])

# Here's a brief explanation of how the function operates:
# 1. The function finds the first sequence of non 'a' characters.
# 2. It then reduces each character in this sequence by 1 lexicographically.
# 3. If the whole string contains only 'a' characters, it turns the last 'a' into a 'z'.
# 4. The updated string is returned as the result. 