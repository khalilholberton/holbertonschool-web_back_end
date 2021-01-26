#!/usr/bin/env python3
"""
this module contains insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert_school instert a new doc in a collection
    """
    d = mongo_collection.insert_one(kwargs)
    return d.inserted_id
