# recommendations
https://meican.com/preorder/api/v2.1/recommendations/dishes?noHttpGetCache=1487946855829&tabUniqueId=50fb782a-d473-4c3f-b0bd-c99f33286d74&targetTime=2017-02-24+10:30

## querystring
+ noHttpGetCache:1487946855829
+ tabUniqueId:50fb782a-d473-4c3f-b0bd-c99f33286d74
+ targetTime:2017-02-24 10:30

# **order**
Request URL:https://meican.com/preorder/api/v2.1/orders/add?corpAddressUniqueId=d39fbacebde5&order=%5B%7B%22count%22:1,%22dishId%22:67809397%7D,%7B%22count%22:1,%22dishId%22:67809418%7D%5D&tabUniqueId=50fb782a-d473-4c3f-b0bd-c99f33286d74&targetTime=2017-02-27+10:30&userAddressUniqueId=d39fbacebde5


%5B%7B%22count%22%3A%201%2C%20%22dishId%22%3A%20658%7D%5D
%5B%7B%22count%22:1,%22dishId%22:67809397%7D,%7B%22count%22:1,%22dishId%22:67809418%7D%5D
Request Method:POST

corpAddressUniqueId:d39fbacebde5
order:[{"count":1,"dishId":67809397},{"count":1,"dishId":67809418}]
tabUniqueId:50fb782a-d473-4c3f-b0bd-c99f33286d74
targetTime:2017-02-27 10:30
userAddressUniqueId:d39fbacebde5

返回
{"message":"","order":{"uniqueId":"3371cb775ccf"},"status":"SUCCESSFUL"}


# order delete
https://meican.com/preorder/api/v2.1/orders/delete

Request Method:POST

(订单id)uniqueId:3371cb775ccf
type:CORP_ORDER
restoreCart:false

返回
{"message":"","order":{"uniqueId":"3371cb775ccf"},"status":"SUCCESSFUL","type":"CORP_ORDER"}
