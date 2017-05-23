def remove_dupes(linked_list):
    if linked_list.head is None:
        return
    node = linked_list.head
    seen_data = set()
    while node is not None:
        if node.data not in seen_data:
            seen_data.add(node.data)
            prev = node
            node = node.next
        else:
            prev.next = node.next
            node = node.next
