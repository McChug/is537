from typing import Optional

from classes import ListNode


def detectCycle(head):
    stop = getStopNode(head)
    if stop == None: return None

    outside = head
    while outside:
        same_seen = False
        stop_seen = False
        inside = head

        while inside:
            if inside == outside and same_seen:
                return inside
            elif inside == outside:
                same_seen = True

            if inside == stop and stop_seen:
                break
            elif inside == stop:
                stop_seen = True

            inside = inside.next

        outside = outside.next

def getStopNode(head):
    fast, slow = head, head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            return fast

    return None

# test in leetcode #142