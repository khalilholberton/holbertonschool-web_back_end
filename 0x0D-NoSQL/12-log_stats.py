#!/usr/bin/env python3
"""
log_infos
"""
from pymongo import MongoClient


def nginx_logs():
    """
    log_infos provides some stats about Nginx logs stored in MongoDB
    """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx = client.logs.nginx

    print("{} logs".format(nginx.count_documents({})))
    print('Methods:')

    for method in methods:
        print("\tmethod {}: {}".format(
                method, nginx.count_documents({'method': method})))

    print("{} status check".format(
        nginx.count_documents({'method': 'GET', 'path': '/status'})))


if __name__ == "__main__":
    nginx_logs()
