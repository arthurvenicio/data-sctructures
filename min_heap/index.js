class MinHeap {
  constructor() {
    this.heap = [];
  }

  getLeftChild(index) {
    return 2 * index + 1;
  }

  getRightChild(index) {
    return 2 * index + 2;
  }

  getParent(index) {
    return Math.floor((index - 1) / 2);
  }

  heapifyUp(index) {
    if (!index) {
      return;
    }

    let parentIndex = this.getParent(index);

    if (this.heap[index] < this.heap[parentIndex]) {
      let temp = this.heap[index];
      this.heap[index] = this.heap[parentIndex];
      this.heap[parentIndex] = temp;

      this.heapifyUp(parentIndex);
    }
  }

  heapifyDown(index) {
    if (!index) {
      return;
    }

    let size = this.heap.length;

    let left = this.getLeftChild(index);
    let right = this.getRightChild(index);

    let smallest = index;

    if (left < size && this.heap[left] < this.heap[smallest]) {
      smallest = left;
    }

    if (right < size && this.heap[right] < this.heap[smallest]) {
      smallest = right;
    }

    if (smallest !== index) {
      let temp = this.heap[index];
      this.heap[index] = this.heap[smallest];
      this.heap[smallest] = temp;

      this.heapifyDown(smallest);
    }
  }

  insert(value) {
    this.heap.push(value);
    this.heapifyUp(this.heap.length - 1);
  }

  pop() {
    if (!this.heap.length) {
      throw new Error("Heap empty");
    }

    if (this.heap.length === 1) {
      this.heap.pop();
    }

    let root = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown(0);

    return root;
  }

  display() {
    console.log(this.heap);
  }
}

let heap = new MinHeap();

heap.insert(0);
heap.insert(1);
heap.insert(2);
heap.insert(3);
heap.insert(4);
heap.insert(5);
heap.insert(0);
// heap.insert(0);

heap.display();
