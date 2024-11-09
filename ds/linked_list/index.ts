class NodeL {
  public value: string | number;
  public next: null | NodeL;
  public prev: null | NodeL;

  constructor(value: string | number) {
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

class DoublyLinkedList {
  private head: null | NodeL;
  private tail: null | NodeL;

  constructor() {
    this.head = null;
    this.tail = null;
  }

  addToFront(value: string | number) {
    let newNode = new NodeL(value);
    newNode.next = this.head;

    if (this.head) {
      this.head.prev = newNode;
    } else {
      this.tail = newNode;
    }

    this.head = newNode;
  }

  addToEnd(value: string | number) {
    let newNode = new NodeL(value);
    newNode.prev = this.tail;

    if (this.tail) {
      this.tail.next = newNode;
    } else {
      this.head = newNode;
    }

    this.tail = newNode;
  }

  popFromFront() {
    if (!this.head) {
      return null;
    }

    let oldValue = this.head.value;

    this.head = this.head.next;

    if (this.head) {
      this.head.prev = null;
    } else {
      this.tail = null;
    }

    return oldValue;
  }
  popFromEnd() {
    if (!this.tail) {
      return null;
    }

    let oldValue = this.tail.value;

    this.tail = this.tail.prev;

    if (this.tail) {
      this.tail.next = null;
    } else {
      this.head = null;
    }

    return oldValue;
  }
}

var db = new DoublyLinkedList();

db.addToFront(3);
db.addToFront(2);
db.addToFront(1);
db.addToEnd(4);
db.addToEnd(5);

console.log(db.popFromFront());
console.log(db.popFromEnd());
console.log(db.popFromFront());
console.log(db.popFromEnd());
