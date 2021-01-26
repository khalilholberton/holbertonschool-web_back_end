#!/usr/bin/env python3
"""
This module contains the func list_all
"""
import pymongo


def list_all(mongo_collection):
    """
    list all documents in the collection mymongo
    """
    if not mongo_collection:
        return []
    all_doc = mongo_collection.find()
    return [d for d in all_doc]
