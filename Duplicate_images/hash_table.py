from element import Element
from prettytable import PrettyTable
from typing import List, Optional


INCREASE = 10
LENGTH = 100


class Table:
    def __init__(self, size: int):
        self.size = size
        self.count = 0
        self.table: List[Optional[Element]] = [None] * size
# Add

    def Add(self, key: str, value: str):
        if self.count == self.size:
            self.table = self._add_new_pos()
        node = self.table[hash(key) % self.size]
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next
        self._push(hash(key) % self.size, key, value)

    def _push(self, hash_address, key, value):
        if self.table[hash_address] is None:
            self.table[hash_address] = Element(key, value)
            self.count += 1
        else:
            new_node = Element(key, value)
            new_node.next = self.table[hash_address]
            self.table[hash_address].previous = new_node
            self.table[hash(key) % self.size] = new_node
            self.count += 1

    def _add_new_pos(self):
        self.size += INCREASE
        new_table = [None] * self.size
        for i in range(len(self.table)):
            if self.table[i] is not None:
                add_node = self.table[i]
                while add_node is not None:
                    pos = hash(add_node.key) % self.size
                    new_table = self.__crate_node(new_table, pos, add_node)
                    add_node = add_node.next
        return new_table

    def __crate_node(self, new_table, pos, add_node):
        if new_table[pos] is None:
            new_table[pos] = Element(add_node.key, add_node.value)
            new_table[pos].next, new_table[pos].previous = None, None
        else:
            new_node = Element(add_node.key, add_node.value)
            new_table[pos].previous = new_node
            new_node.next = new_table[pos]
            new_table[pos] = new_node
        return new_table

#

# Find
    def find(self, key: str):
        node = self.table[hash(key) % self.size]
        while node is not None:
            return node.value if node.key == key else node == node.next
        return "No element ".format(key)
# Delete

    def delete(self, key: str) -> None:
        curr_node = self.table[hash(key) % self.size]

        if curr_node.key == key:
            if curr_node.next is not None:
                self.__del(hash(key) % self.size, curr_node.next)
                return
            elif curr_node.next is None:
                self.__del(hash(key) % self.size, None)
                return
        elif curr_node is None:
            return

        self._check_for_none(key, curr_node)

    def __del(self, hash_address, val):
        self.table[hash_address] = val
        self.count -= 1

    def _check_for_none(self, key, curr_node):
        while curr_node is not None:
            if curr_node.key == key:
                curr_node.previous.next = curr_node.next
                if curr_node.next is not None:
                    curr_node.next.previous = curr_node.previous
                return
            curr_node = curr_node.next
#
# Print

    def print_table(self) -> None:
        table = PrettyTable()
        table.field_names = ['Хэш адрес', "Ключ", "Значение"]

        for i in range(self.size):
            if self.table[i] is not None:
                curr_node = self.table[i]
                while curr_node is not None:
                    table = self.create_table(table, curr_node)
                    curr_node = curr_node.next

        return table

    def create_table(self, table, curr_node):
        table.add_row([
            hash(curr_node.key) % self.size,
            curr_node.key,
            curr_node.value if len(curr_node.value) < LENGTH else curr_node.value[:LENGTH] + '...'
        ])
        return table

#