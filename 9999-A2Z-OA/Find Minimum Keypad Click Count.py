'''
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

'''

# We can sort as per frequencies and fill 9 boxes or map or list.