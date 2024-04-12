class LinkedListStack:
    def __init__(self):
        self._peek: ListNode | None = None
        self._size: int = 0
    
    def size(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return not self._peek
    
    def push(self, val: int):
        node = ListNode(val)
        node.next = self._peek
        self._peek = node
        self._size += 1

    def pop(self) -> int:
        num = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return num
    
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._peek.val
    
    def to_list(self) -> list[int]:
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr