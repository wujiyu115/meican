# INTRO
完善了一下 [hui-z](https://github.com/hui-z/mcm) 的逻辑

美餐自动订餐,在截止订餐时间前自动订餐

## 订餐逻辑
如果有快捷订餐则进行快捷订餐,否则选择第一家可定餐厅定餐.


# 配置
配置在`cfg/config.conf`目录下

```shell
#关闭订餐前多少分开始自动订餐
ahead_min = 10
#周几订餐1-7代表周一到周日
order_week = 1,2,3,4,5
#是否订同事常订的餐 true,false
other_recommend = false
#忽略的菜品关键字
ignore_dish = 韩国泡菜,烧鸭
```


## 运行

双击 `start.bat`

### 需知
为了在其他电脑上也可以运行,我把`python`环镜便携安装到了项目目录重命令为`py`,`python`的便携安装很简单,只要在安装时选择`Install just for me` 就会把`dll`等依赖也安装在`python`目录下


# build.bat
+ 需先便携化`python`在本项目重命名为`py`
+ 依赖`7z`压缩


# TODO
+ [x] 推荐订餐
+ [x] 保存cookie
+ [x] 日志请求记录
+ [x] 订餐配置
+ [x] 餐厅随机订餐
+ [x] 删除订单
+ [x] 订多个菜
+ [x] 忽略菜品
