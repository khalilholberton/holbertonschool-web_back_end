#!/usr/bin/env python3
"""
this module contains list_all
"""


def list_all(mongo_collection):
    """
    list_all
    """
    all_doc = mongo_collection.find()
    return all_doc if all_doc else []
