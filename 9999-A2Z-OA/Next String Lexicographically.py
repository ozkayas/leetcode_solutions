

def solution(string: str) -> str:
    if string == 'z':
        return '-1'  # Return string '-1' instead of int for consistent return type

    stack = []
    duplicateExists = False

    for index, char in enumerate(string):
        # if duplicate then fill the rest with ab starting from this index
        if duplicateExists:
            stack.append('a' if index % 2 == mod_for_a else 'b')
            continue

        if stack and stack[-1] == char:
            if char == 'z':
                return '-1'

            stack.append(chr(ord(char) + 1))
            duplicateExists = True
            mod_for_a = (index + 1) % 2
        else:
            stack.append(char)

    if duplicateExists:
        return ''.join(stack)

    # Handle cases where the next lexicographical string needs to be generated
    while stack and (stack[-1] == 'z' or (len(stack) > 1 and stack[-2] == 'z' and stack[-1] == 'y')):
        stack.pop()

    if not stack:
        return '-1'

    # Increment the last character
    last_char = stack.pop()
    stack.append(chr(ord(last_char) + 1))

    # If incrementing leads to a duplicate, increment again
    if len(stack) > 1 and stack[-1] == stack[-2]:
        last_char = stack.pop()
        stack.append(chr(ord(last_char) + 1))

    # Fill the rest of the string with alternating 'a' and 'b'
    length = len(stack)
    mod_for_a = length % 2

    while len(stack) < len(string):
        stack.append('a' if len(stack) % 2 == mod_for_a else 'b')

    return ''.join(stack)

print(solution('abcc'))
print(solution('abccss'))
print(solution('zyx'))
print(solution('abbd'))
print(solution('abccdeaaa'))
print(solution('zzab'))
print(solution('zyxwvutstuvwxyz'))
print(solution('zyz'))
print(solution('zyxz'))
print(solution('zyzyzyz'))

