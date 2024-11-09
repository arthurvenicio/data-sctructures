function dailyTemperatures2(temperatures: number[]): number[] {
  let results: number[] = temperatures.map((_) => 0);
  let stack: number[] = [];

  temperatures.forEach((temp, idx) => {
    while (stack && temperatures[stack[stack.length - 1]] < temp) {
      let index = stack.pop();
      if (index) {
        results[index] = idx - index;
      }
    }

    stack.push(idx);
  });

  return results;
}

console.log(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]));
