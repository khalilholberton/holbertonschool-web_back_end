#!/usr/bin/env python3
"""
func makes updates
"""


def update_topics(mongo_collection, name, topics):
    """
    update_topics changes all topics of a school document based on the name.
    """
    if mongo_collection and name:
        mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}})
