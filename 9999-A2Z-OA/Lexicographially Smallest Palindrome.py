def getSmallestPalindrome(word: str) -> str:

    s, e = 0, len(word) - 1
    buffer = list(word)

    while s <= e:
        if buffer[s] == "?" and buffer[e] == "?":
            buffer[s] = "a"
            buffer[e] = "a"
        elif buffer[s] == "?":
            buffer[s] = buffer[e]
        elif buffer[e] == "?":
            buffer[e] = buffer[s]
        elif buffer[s] != buffer[e]:
            return "-1"

        s += 1
        e -= 1

    return "".join(buffer)

from Scripts.test_utils import test_case
test_case(getSmallestPalindrome,("a?rt???",),"aartraa")
test_case(getSmallestPalindrome,("bx??tm",),"-1")
