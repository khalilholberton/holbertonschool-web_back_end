#!/usr/bin/env python3
"""
nginx_log
"""
from pymongo import MongoClient


def nginx_log():
    """ adding the top 10 of the most present IPs """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    number = nginx_collection.count()

    num_get = nginx_collection.find({"method": "GET"}).count()
    num_post = nginx_collection.find({"method": "POST"}).count()
    num_put = nginx_collection.find({"method": "PUT"}).count()
    num_patch = nginx_collection.find({"method": "PATCH"}).count()
    num_delete = nginx_collection.find({"method": "DELETE"}).count()
    num_status = nginx_collection.find(
        {"method": "GET", "path": "/status"}).count()
    num_ips = nginx_collection.aggregate([
            {"$group": {"_id": "$ip", "total": {"$sum": 1}}},
            {"$sort": {"total": -1}},
            {"$limit": 10}
        ])

    print("{} logs".format(number))
    print("Methods:")
    print("\tmethod GET: {}".format(num_get))
    print("\tmethod POST: {}".format(num_post))
    print("\tmethod PUT: {}".format(num_put))
    print("\tmethod PATCH: {}".format(num_patch))
    print("\tmethod DELETE: {}".format(num_delete))
    print("{} status check".format(num_status))
    print("IPs:")
    for ip in num_ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("total")))


if __name__ == "__main__":
    nginx_log()
