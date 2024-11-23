/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let stack = [];
  let char_map = {
    ")": "(",
    "}": "{",
    "]": "["
  }; // we must map all pairs

  for (let char of s) {
    // we must iterate over each character of the string.
    // validate if it is the closing pair, if not we put on the stack
    if (char_map[char]) {
      if (stack.length && stack[stack.length - 1] == char_map[char]) {
        stack.pop();
      } else {
        return false;
      }
    } else {
      stack.push(char);
    }
  }

  return !stack.length;
};

console.log(isValid("()"));
