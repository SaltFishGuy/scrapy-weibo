# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UserItem(Item):
    collection = 'users' #定义collection字段，指名保存的Collection名称

    id = Field() #用户的ID
    name = Field() #用户名称
    avatar = Field() #用户的头像
    cover = Field() #用户背景图
    gender = Field() #用户性别
    description = Field() #用户简介
    fans_count = Field() #粉丝数量
    follows_count = Field() #关注人数
    weibos_count = Field() #发布微博数量
    verified = Field() #是否官方认证
    verified_reason = Field()
    verified_type = Field()
    follows = Field() #关注列表
    fans = Field() #粉丝列表
    crawled_at = Field()  #爬取时间


class UserRelationItem(Item):
    collection = 'users'

    id = Field()
    follows = Field()
    fans = Field()


class WeiboItem(Item):
    collection = 'weibos'

    id = Field()
    attitudes_count = Field()
    comments_count = Field()
    reposts_count = Field()
    picture = Field()
    pictures = Field()
    source = Field()
    text = Field()
    raw_text = Field()
    thumbnail = Field()
    user = Field()
    created_at = Field()
    crawled_at = Field()
