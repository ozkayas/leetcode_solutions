"""
https://www.fastprep.io/problems/amazon-find-minimum-keypad-click-count
A recently launched supplemental typing keypad gained significant popularity on Amazon Shopping due to its flexibility.

This keypad can be connected to any electronic device and has 9 buttons, where each button can have up to 3 lowercase English letters. The buyer has the freedom to choose which letters to place on a button while ensuring that the arrangement is valid. A keypad design is said to be valid if:

All 26 letters of the English alphabet exist on the keypad.
Each letter is mapped to exactly one button.
A button has at most 3 letters mapped to it.
Examples of some valid keypad designs are:

"abacadegfhibj"
a:3-
b:2-
c:1-
d:1
e:1
f:1
g:1
h:1
i:1
j:1

"""
from collections import Counter


# We can sort as per frequencies and fill 9 boxes or map or list.
def minimumKeypresses(s: str) -> int:
    # Compute the frequency of each character in the string
    character_frequency = Counter(s)

    # Initialize the total number of key presses
    total_key_presses = 0

    # Initialize the keys already allocated and the current multiplier
    allocated_keys, current_multiplier = 0, 1

    # Loop through the character frequencies in descending order
    for frequency in sorted(character_frequency.values(), reverse=True):
        allocated_keys += 1  # Increment keys allocated to count this character
        total_key_presses += current_multiplier * frequency  # Add the key presses for this character

        # Every 9th character requires an additional key press (since you can only fit 9 on one screen)
        if allocated_keys % 9 == 0:
            current_multiplier += 1  # Increase the multiplier after filling a screen

    # Return the total number of key presses
    return total_key_presses

from Scripts.test_utils import test_case
test_case(minimumKeypresses, ("abacadefghibj",), 14)