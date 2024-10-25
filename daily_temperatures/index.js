function dailyTemperatures(temperatures) {
  let results = temperatures.map((_) => 0);
  let stack = [];

  temperatures.forEach((temp, idx) => {
    while (stack && temperatures[stack[stack.length - 1]] < temp) {
      index = stack.pop();
      results[index] = idx - index;
    }

    stack.push(idx);
  });

  return results;
}

console.log(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]));
