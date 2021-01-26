#!/usr/bin/env python3
"""nginx_log"""

from pymongo import MongoClient


def nginx_log() -> None:
    """  adds the top 10 of the most present IPs  """

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print("{} logs".format(nginx.count_documents({})))
    print("Methods:")
    for m in methods:
        print("\tmethod {}: {}".format(m, nginx.count_documents({'method': m})))
    print("{} status check".
          format(nginx.count_documents({'method': 'GET', 'path': '/status'})))
    print("IPs:")
    all_ip = []
    num_ips = nginx.aggregate([
        { "$group": {  "_id" : "$ip", "total" : { "$sum": 1 }  } },
        { "$sort": { "total": -1 } }
    ])
    count = 0
    for s_ip in num_ips:
        if count == 10:
            break
        print("\t{}: {}".format(s_ip.get('_id'),s_ip.get('total')))
        count = count + 1


if __name__ == "__main__":
    nginx_log()
