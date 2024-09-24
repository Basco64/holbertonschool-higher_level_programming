#!/usr/bin/python3

from abc import ABC, abstractmethod


class CountedIterator:
    """countediterator class"""

    def __init__(self, iterable):
        """initialization"""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """next"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """current count of items"""
        return self.count

    def __iter__(self):
        """iterator"""
        return self
