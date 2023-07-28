#!/usr/bin/env python3
"""simple helper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index range"""
    return ((page - 1) * page_size, page * page_size)
