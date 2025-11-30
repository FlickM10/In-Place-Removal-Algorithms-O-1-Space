dummy = ListNode(-1)
dummy.next = head
current = head
prev = dummy

while current:
    if current.val == val:
        prev.next = current.next
    else:
        prev = current
    current = current.next
return dummy.next
