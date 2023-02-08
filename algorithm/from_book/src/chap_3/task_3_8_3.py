# -*- coding: utf-8 -*-
from typing import Any

from resources import ISolution
from resources import LinkedListBase
from resources import Node


class LinkedList(LinkedListBase):
    def begining(self, node: Node) -> None:
        node.next = self.head
        self.head = node


class Solution(ISolution):
    def start_task(self, *args: Any, **kwargs: Any) -> Any:
        linked_list = LinkedList()
        linked_list.head = linked_list.generate_nodes()
        linked_list.begining(kwargs.get("node"))
        return linked_list


if __name__ == "__main__":
    solution: LinkedList = Solution().start_task(node=Node(0))
    solution.print_list()
