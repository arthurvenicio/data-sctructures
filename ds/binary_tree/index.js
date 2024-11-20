class NodeTree {
  constructor(val, left, right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

class BinaryTree {
  constructor(root) {
    this.root = root;
  }

  bfs(root) {
    if (!root) {
      return;
    }

    let queue = [root];

    while (queue.length) {
      let node = queue.pop();

      console.log("node data: " + node.val);

      if (node.left) {
        queue.push(node.left);
      }

      if (node.right) {
        queue.push(node.right);
      }
    }
  }
}

let root = new NodeTree(10);
root.left = new NodeTree(5);
root.right = new NodeTree(12);
root.left.left = new NodeTree(3);

let bTree = new BinaryTree(root);

console.log("\nLevel order: ");
bTree.bfs(root);
