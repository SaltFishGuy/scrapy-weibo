# scrapy-weibo

## 项目名称:
scrapy-weibo+代理池+cookies池

## 项目描述：
新浪微博是如今大数据方面最好的一个体现,爬取新浪微博简单分析一些有意思的现象。

## Scrapy开发工具准备:
操作系统windows10<br>
Python版本:3.6.5<br>
开发工具:pycharm<br>
内置模块:json<br>
第三方模块:scrapy-1.6.0,pymongo-3.7.2,requests-2.21.0<br>
数据库:mongodb<br>

## 代理池开发工具准备:
操作系统windows10<br>
python版本:3.6.5<br>
开发工具:pycharm<br>
内置模块:json、re、sys<br>
第三方模块:flask-1.0.2、pyquery-1.4.0<br>
数据库:redis<br>

## Cookies池开发工具准备:
操作系统windows10<br>
python版本:3.6.5<br>
开发工具:pycharm<br>
内置模块:json、re、sys<br>
第三方模块:flask-1.0.2、pyquery-1.4.0,requests-2.21.0<br>
数据库:redis<br>

### 第一步开启cookies池
#### 启动redis
在cmd下输入```redis-server```<br>
![image](https://github.com/SaltFishGuy/picture/blob/master/redis-start.png)<br>
执行cookies池下的run.py<br>
![image](https://github.com/SaltFishGuy/picture/blob/master/cookies-start.png)<br>

### 第二部开启代理池
在cmd下输入```redis-server```<br>
![image](https://github.com/SaltFishGuy/picture/blob/master/redis-start.png)<br>
执行proxypool池下的run.py<br>
![image](https://github.com/SaltFishGuy/picture/blob/master/proxypool.png)<br>

### 第三部开启新浪微博爬虫
在pycharm的交互命令行窗口执行weibocn爬虫```scrapy crawl weibocn```<br>
![image](https://github.com/SaltFishGuy/picture/blob/master/scrapy.png)<br>

### 存储在mongodb中的数据
使用mongodb可视化工具Robo 3T 1.2.1<br>
![image](https://github.com/SaltFishGuy/picture/blob/master/mongodb.png)<br>

