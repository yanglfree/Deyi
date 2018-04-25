# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 用户信息
class UserItem(scrapy.Item):
    userId = scrapy.Field()
    avatar = scrapy.Field()
    userName = scrapy.Field()
    level = scrapy.Field() #等级
    userGender = scrapy.Field() #用户性别
    posts = scrapy.Field() #用户发帖数
    comments = scrapy.Field() #用户回帖数
    reposts = scrapy.Field() #转发数
    stars = scrapy.Field() #关注数
    fans = scrapy.Field() #粉丝数
    postList = scrapy.Field() #帖子列表
    starPostList = scrapy.Field() #订阅帖子列表
    relationship = scrapy.Field() #与本人关系
    isPrivace = scrapy.Field() #是否设置隐私
    pass


# 帖子
class ArticleItem(scrapy.Item):
    title = scrapy.Field() # 帖子的标题
    desc = scrapy.Field() #帖子的概述
    type = scrapy.Field() # type分为两种，Single 0 单图，Multi 1多图  class = 'other'时为多图
    articleImg = scrapy.Field() # 帖子的图片列表 单图或者多图
    coverImg = scrapy.Field() #封面图 某些地方需要
    articleUrl = scrapy.Field() #帖子的地址
    avatar = scrapy.Field() #发帖人的头像地址
    author = scrapy.Field() #发帖人的名称
    postTime = scrapy.Field() #发帖时间
    comments = scrapy.Field() #回复数
    reads = scrapy.Field() #阅读数
    ups = scrapy.Field() #点赞数
    pass

# 板块
class ForumItem(scrapy.Item):
    type = scrapy.Field() #两种类型 life生活  shop消费
    forumUrl = scrapy.Field() #板块链接
    forumImage = scrapy.Field() #板块小图标
    forumTitle = scrapy.Field() #板块名称
    forumDesc = scrapy.Field() #板块概述


# 凑热闹
class WeiboItem(scrapy.Item):
    avatar = scrapy.Field() # 头像
    author = scrapy.Field() # 作者
    level = scrapy.Field()  # 用户等级
    postTime = scrapy.Field() #发布时间
    star = scrapy.Field() # 关注
    address = scrapy.Field() #显示的地理位置
    imgs = scrapy.Field() #图片
    content = scrapy.Field() #正文
    label = scrapy.Field() #标签

# 回复
class CommentItem(scrapy.Item):
    user = scrapy.Field()  # 用户
    ups = scrapy.Field() #点赞数
    postTime = scrapy.Field() # 回复时间
    authorId = scrapy.Field() #回复人id
    isAuthor = scrapy.Field() # 是否楼主
    postId = scrapy.Field() #回复者id
    quote = scrapy.Field() # 被引用的评论


# 活动
class SpeedDialItem(scrapy.Item):
    speeddialImg = scrapy.Field()
    speeddialName = scrapy.Field()
    speeddialUrl = scrapy.Field()



