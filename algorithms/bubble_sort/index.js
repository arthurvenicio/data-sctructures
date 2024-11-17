function bubbleSort(arr) {
  let size = arr.length;

  for (let i = 0; i < size; i++) {
    let swapped = false;

    for (let j = 0; j <= size - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        swapped = true;
      }
    }

    if (!swapped) {
      break;
    }
  }

  return arr;
}

arr = bubbleSort([1, 2, 5, 4, 3]);

console.log(arr);
