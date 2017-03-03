# -*- coding: utf-8 -*-
# @Author: wujiyu
# @Date:   2017-02-25 12:38:03
# @Last Modified by:   wujiyu
# @Last Modified time: 2017-02-26 22:42:29

import inspect


def cls_attr_values(cls,filter_attrs=[]):
    attributes = inspect.getmembers(cls, lambda a:not(inspect.isroutine(a)))
    return [a for a in attributes if not a[0].startswith('__') and not a[0].endswith('__') and not a[0] in filter_attrs]

def cls_attrs(cls,filter_attrs=[]):
    attributes = inspect.getmembers(cls, lambda a:not(inspect.isroutine(a)))
    return [a[0] for a in attributes if not a[0].startswith('__') and not a[0].endswith('__') and not a[0] in filter_attrs ]

# obj or cls to dict
def obj_dict(obj,filter_attrs=[]):
    return dict((key_value[0], key_value[1]) for key_value in cls_attr_values(obj,filter_attrs))

seqs = tuple, list, set, frozenset
# dict to obj
def dict_obj(d):
    top = type('new', (object,), d)
    for i, j in d.items():
        if isinstance(j, dict):
            setattr(top, i, dict_obj(j))
        elif isinstance(j, seqs):
            setattr(top, i,
                type(j)(dict_obj(sj) if isinstance(sj, dict) else sj for sj in j))
        else:
            setattr(top, i, j)
    return top

def dict_item_obj(lst):
    if isinstance(lst, seqs):
        ret = []
        for item in lst:
            ret.append(dict_obj(item))
        return ret

