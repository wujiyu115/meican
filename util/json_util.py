# -*- coding: utf-8 -*-
# @Author: wujiyu
# @Date:   2016-11-23 14:52:18
# @Last Modified by:   wujiyu
# @Last Modified time: 2017-02-28 10:54:18
import json

from datetime import datetime
from uuid import UUID

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, UUID):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


def json_dump(result):
    return json.dumps(result,cls=CJsonEncoder)

