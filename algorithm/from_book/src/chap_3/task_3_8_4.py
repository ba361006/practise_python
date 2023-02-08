# -*- coding: utf-8 -*-
from typing import Any

from resources import ISolution
from resources import LinkedListBase
from resources import Node


class LinkedList(LinkedListBase):
    def ending(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = node


class Solution(ISolution):
    def start_task(self, *args: Any, **kwargs: Any) -> Any:
        linked_list = LinkedList()
        linked_list.head = linked_list.generate_nodes()
        linked_list.ending(kwargs.get("node"))
        return linked_list


if __name__ == "__main__":
    solution: LinkedList = Solution().start_task(node=Node(100))
    solution.print_list()
