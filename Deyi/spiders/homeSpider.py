import scrapy
from scrapy.spiders import CrawlSpider

from items import ArticleItem


class HomeSpider(CrawlSpider):
    name = 'home'
    allowed_domains = ["deyi"]
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
        "Upgrade-Insecure-Requests" : 1,
    }

    start_urls = ("http://m.deyi.com",)
    def parse(self, response):
        articleList = []
        selList = response.xpath('//section[@class="index-column"]/ul/li')
        for sel in selList:
            item = ArticleItem()
            try:
                item['title'] = sel.xpath('a/div[1]/h2/text()').extract()[0]
                item['desc'] = sel.xpath('a/div[1]/p/text()').extract()[0]
                item['articleUrl'] = sel.xpath('a/@href').extract()[0]
                item['avatar'] = sel.xpath('a//div[@class="info"]/img/@dataimg').extract()[0]
                item['author'] = sel.xpath('a//span/text()').extract()[0]
                item['postTime'] = sel.xpath('a//time/text()').extract()[0]
                articleList.append(item)
            except Exception as e:
                print(e)
        return articleList


