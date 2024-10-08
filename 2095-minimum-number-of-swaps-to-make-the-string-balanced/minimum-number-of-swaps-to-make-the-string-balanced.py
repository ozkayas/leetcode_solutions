class Solution:
    def minSwaps(self, s: str) -> int:
        # We are counting unbalanced ] items, stack is only filled with openings to match next coming ]'s
        stack = []
        unbalanced = 0
        for ch in s:
            # If an opening bracket is encountered, push it in the stack
            if ch == "[":
                stack.append(ch)
            else:
                # If the deque is not empty, pop it.
                if stack:
                    stack.pop()
                # Otherwise increase the count of unbalanced brackets.
                else:
                    unbalanced += 1
        return (unbalanced + 1) // 2
        