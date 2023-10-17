#!/usr/bin/env python3
"""
list all documents on mongo using python
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    :param mongo_collection: The PyMongo collection object.
    :return: A list of documents from the collection.
    """
    documents = mongo_collection.find()
    return documents
