#!/usr/bin/env python3
"""
lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection
    """
    doc = mongo_collection.find()
    return doc if doc else []
