#!/usr/bin/env python3
"""
lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection
    """
    all_doc = mongo_collection.find()
    if all_doc:
        return all_doc
    else:
        return []
