# -*- coding: utf-8 -*-

print(u'\u897f\u7ea2\u67ff\u9e21\u86cb\u62c9\u9762' in u'\u897f\u7ea2\u67ff')

ignore_dishs = {"1", "2", u'\u897f\u7ea2\u67ff'}
dish_name = u"\u897f\u7ea2\u67ff\u9e21\u86cb\u62c9\u9762"
print(len(filter(lambda x:x in dish_name, ignore_dishs)) > 0)