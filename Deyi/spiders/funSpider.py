import pymongo
from scrapy import Request
from scrapy.spiders import CrawlSpider

from Deyi.items import WeiboItem, UserItem, CommentItem


class FunSpider(CrawlSpider):

    host = 'http://www.deyi.com'

    name = 'fun'
    allowed_domains = ['deyi.com']

    start_urls = ('http://m.deyi.com/fun.html',)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
        "Upgrade-Insecure-Requests": 1,
    }

    pages = set()

    def parse(self, response):
        for i in range(1,20):
            url = ('http://m.deyi.com/fun-recommend-%d.html') % (i + 1)
            if url not in self.pages:
                self.pages.add(url)
                yield Request(url,dont_filter=True)

        funSelectorList = response.xpath('//section[@class="lively-ct"]/div/section')
        for sel in funSelectorList:
            url = sel.xpath('./a[1]/@href').extract()[0]
            author = UserItem()
            author['avatar'] = response.xpath('//div[@class="left"][1]/img/@dataimg').extract()[0]
            author['userName'] = response.xpath('//h4[1]/text()').extract()[0]
            author['level'] = response.xpath('//span[1]/text()').extract()[0]
            newUrl = self.host + url
            print(newUrl)
            yield Request(newUrl,callback=self.parse_funInfo,dont_filter=True)

        print(funSelectorList)

    def parse_funInfo(self,response):
        item = WeiboItem()
        item['time'] = response.xpath('//time[1]/text()').extract()
        item['title'] = response.xpath('//h1/text()').extract()
        item['comments'] = response.xpath('//span[@class="reply"][1]/text()').extract()
        item['reads'] = response.xpath('//span[@class="browse appmore"][1]/text()').extract()
        # item['author'] = author
        item['articleImg'] = response.xpath('//article[@class="content-main"][1]/img/@src').extract()
        item['labels'] = response.xpath('//div[@class="content-label"]/a/text()').extract()

        commentList = []
        commentSelList = response.xpath('//section[contains(@class,"pid")]')
        for sel in commentSelList:
            comment = CommentItem()
            comment['commentAvatar'] = sel.xpath('//img[1]/@src').extract()
            comment['commentName'] = sel.xpath('//user-name[1]/text()').extract()
            comment['commentLevel'] = sel.xpath('//user-level[1]/text()').extract()
            comment['content'] = sel.xpath('//article[1]/p[1]/text()').extract()
             # 还要对多页评论的情况进行处理 TODO
            comment['ups'] = sel.xpath('//aside[1]/text()').extract()
            comment['postTime'] = sel.xpath('//time[1]/text()').extract()
            commentList.append(comment)
        print(commentList)
        item['comments'] = commentList
        item['likes'] = sel.xpath('//span[1]/text()').extract()
        item['likeList'] = sel.xpath('//nav[@class="like-list"]/a/text()').extract()
        self.saveToMongo(item)



    def saveToMongo(self, item):
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client.deyi
        collection = db.funs
        collection.insert_one(item)





