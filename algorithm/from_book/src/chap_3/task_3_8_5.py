# -*- coding: utf-8 -*-
from typing import Any

from resources import ISolution
from resources import LinkedListBase
from resources import Node


class LinkedList(LinkedListBase):
    def between(self, index: int, node: Node) -> None:
        if self.head is None:
            if index == 0:
                self.head = node
                return
            raise ValueError(
                f"Index out of range, we got 0 node but given index is {index}"
            )

        ptr = self.head
        count = 0
        while ptr.next:
            if count == index:
                break
            ptr = ptr.next
            count += 1

        if ptr.next is None:
            if index != count:
                raise ValueError(
                    f"index out of range, we got only {count} nodes but given index is {index}"
                )
            ptr.next = node
        else:
            node.next = ptr.next
            ptr.next = node


class Solution(ISolution):
    def start_task(self, *args: Any, **kwargs: Any) -> Any:
        linked_list = LinkedList()
        linked_list.head = linked_list.generate_nodes()
        linked_list.between(kwargs.get("index"), kwargs.get("node"))
        return linked_list


if __name__ == "__main__":
    solution: LinkedList = Solution().start_task(index=1, node=Node(100))
    solution.print_list()
