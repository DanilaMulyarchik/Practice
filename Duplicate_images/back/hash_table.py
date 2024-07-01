from prettytable import PrettyTable
from typing import List, Optional
from back.image import hash_comparison

INCREASE = 10
LENGTH = 100


class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class Table:
    def __init__(self, size: int, percent):
        self.size = size
        self.count = 0
        self.table: List[Optional[Element]] = [None] * size
        self.same = []
        self.percent = percent
# Add

    def Same(self):
        '''
        :return: список сзожих изображений
        '''
        return self.same

    def Add(self, key: str, value: str):
        '''
        Заполнение хэш-таблицы
        :param key: хэш изображения
        :param value: путь изображения
        '''
        node = self.table[hash(key) % self.size]
        while node is not None:
            if float(hash_comparison(node.key, key)) >= self.percent:
                self.same.append(value)
                self.same.append(node.value)
                node.value = value
                return
            node = node.next
        self._push(hash(key) % self.size, key, value)

    def _push(self, hash_address, key, value):
        '''
        Вставка элемента в таблицу
        :param hash_address: Слот в таблице
        :param key: хэш изображения
        :param value: путь изображения
        '''
        if self.table[hash_address] is None:
            self.table[hash_address] = Element(key, value)
            self.count += 1
        else:
            new_node = Element(key, value)
            new_node.next = self.table[hash_address]
            self.table[hash_address].previous = new_node
            self.table[hash(key) % self.size] = new_node
            self.count += 1