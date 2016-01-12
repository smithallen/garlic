#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: smithallen
# @Date:   2016-01-12 16:39:02
# @Last Modified by:   smithallen
# @Last Modified time: 2016-01-12 17:16:49

'''
in pymongo, there are some bson object that
cannot serialize using json.dumps
how ever there is bson.json_util can help in some way
'''

import json
from bson.objectid import ObjectId
from bson import json_util


class MongoEncoder(json.JSONEncoder):

    def default(self, v):
        types = dict()
        types["ObjectId"] = lambda v: str(v)
        types["datetime"] = lambda v: v.isoformat()

        vtype = type(v).__name__
        if vtype in types:
            return types[vtype](v)
        else:
            return json.JSONEncoder.default(self, v)

json._default_encoder = MongoEncoder()


def main():
    test = dict()
    test["test"] = 1
    test["_id"] = ObjectId("0123456789ab0123456789ab")

    print json.dumps(test)
    '''{"test": 1, "_id": "0123456789ab0123456789ab"}'''

    print json_util.dumps(test)
    '''{"test": 1, "_id": {"$oid": "0123456789ab0123456789ab"}}'''

if __name__ == '__main__':
    main()
