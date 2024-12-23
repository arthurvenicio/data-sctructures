function transpose(matrix) {
  let rows = matrix.length;
  let col = matrix[0].length;
  let new_matrix = matrix.map(() => {
    return new Array(rows).fill(0);
  });

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < col; j++) {
      new_matrix[j][i] = matrix[i][j];
    }
  }

  return new_matrix;
}

console.log(
  transpose([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ])
);
