#!/usr/bin/env python3
"""
this module contains list_all
"""


def list_all(mongo_collection):
    """
    list_all
    """
    docs = mongo_collection.find()
    if docs:
        return docs
    else:
        return []
