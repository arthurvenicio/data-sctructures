## Question

In this task, you are given a string `s`, and your goal is to produce a new string following a specific pattern. You are to take characters in sets of three, reverse the characters in each set, and then place them back into the string in their original positions, preserving the reverse order within each set. If 1 or 2 characters remain at the end (because the length of the string is not divisible by 3), they should be left as they are.

The string `s` contains only lowercase English letters, with its length ranging from `1` to `300`, inclusive.

For example, if you are given the input `'abcdef'`, the output should be `'cbafed'`. For the input `'abcdefg'`, your function should provide `'cbafedg'`.
