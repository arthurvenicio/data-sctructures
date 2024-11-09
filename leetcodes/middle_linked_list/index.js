/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function (head) {
  let nextHead = head;

  while (nextHead && nextHead.next) {
    nextHead = nextHead.next.next; // the nextHead pointer is running twice in front of "head"
    head = head.next;
  }

  return head;
};
