import { ListNode } from "./WithoutRecursion.ts";

export function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null,
  carry: 0 | 1 = 0,
): ListNode | null {
  const val1 = l1 ? l1.val : 0;
  const val2 = l2 ? l2.val : 0;
  const next1 = l1 ? l1.next : null;
  const next2 = l2 ? l2.next : null;

  let sum = val1 + val2 + carry;

  if (sum >= 10) {
    sum -= 10;
    carry = 1;
  } else {
    carry = 0;
  }

  if (next1 || next2)
    return new ListNode(sum, addTwoNumbers(next1, next2, carry));

  if (carry) return new ListNode(sum, new ListNode(carry));

  return new ListNode(sum);
}
