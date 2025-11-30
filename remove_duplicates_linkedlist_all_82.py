dummy = ListNode(-1)
dummy.next = head
current = head
prev = dummy

while current and current.next:
    if current.val == current.next.val:
        value = current.val
        while current and current.val == value:
            current = current.next
        prev.next = current
    else:
        prev = current
    current = current.next
return dummy.next