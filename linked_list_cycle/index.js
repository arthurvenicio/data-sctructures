/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  let fast = head;
  let slow = head;

  while (fast && fast.next) {
    // to check if we've a cycle, create 2 pointer one slower and outher faster, if any moment both are the same we have a cycle.
    slow = slow.next;
    fast = fast.next.next;
    if (slow == fast) {
      return true;
    }
  }

  return false;
};
