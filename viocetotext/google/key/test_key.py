#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/30/2017 9:09 AM
# @Author  : Siyuan(Saiun)
# @Site    : 
# @File    : test_key.py
# @Software: PyCharm Community Edition
def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

if __name__ == "__main__":
    implicit()