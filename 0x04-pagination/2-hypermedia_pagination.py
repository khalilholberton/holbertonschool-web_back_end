#!/usr/bin/env python3
""" module """
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' def page '''
        assert type(page_size) is int and type(page) is int
        assert page > 0
        assert page_size > 0
        self.dataset()
        a = index_range(page, page_size)
        if a[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[a[0]:a[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ get hyper """
        data = self.get_page(page, page_size)
        total_p = math.ceil(len(self.__dataset) / page_size)
        x = page + 1 if page < total_p else None
        y = page - 1 if page > 1 else None
        return {'page_size': len(data), 'page': page, 'data': data,
                'next_page': x, 'prev_page': y, 'total_pages': total_p}


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index range"""
    a = page * page_size - page_size
    b = a + page_size
    return (a, b)
