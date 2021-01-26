#!/usr/bin/env python3
"""
This module contains the func list_all
"""


def list_all(mongo_collection):
    """
    list all documents in the collection mymongo
    """
    all_doc = mongo_collection.find()
    if all_doc:
        return all_doc
    return []
