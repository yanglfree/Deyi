from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request
from Deyi.items import ArticleItem
from Deyi.items import CommentItem
from urllib.parse import urljoin


class HomeSpider(CrawlSpider):
    name = 'home'
    allowed_domains = ["deyi.com"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
        "Upgrade-Insecure-Requests": 1,
    }

    start_urls = ("http://m.deyi.com/forum-41-1.html",)

    # rules = Rule(LinkExtractor(allow=()),callback='parse_home',follow=True)

    # def parse(self, response):

    # """
    # @url http://deyi.com
    # @return items 1
    # @scrapes title desc articleUrl avatar author postTime
    # @scrapes url project spider server date
    # """
    # loader = ItemLoader(item=ArticleItem(),response=response)
    # loader.add_xpath('title','a/div[1]/h2/text()')
    # loader.add_xpath('desc', 'a/div[1]/p/text()')
    # loader.add_xpath('articleUrl', 'a/@href')
    # loader.add_xpath('avatar', 'a//div[@class="info"]/img/@dataimg')
    # loader.add_xpath('author', 'a//span/text()')
    # loader.add_xpath('postTime', 'a//time/text()')
    #
    # loader.add_value('url', response.url)
    # loader.add_value('project', self.settings.get('BOT_NAME'))
    # loader.add_value('spider', self.name)
    # loader.add_value('server', socket.gethostname())
    # loader.add_value('date', datetime.datetime.now())
    # return loader.item


    # selList = response.xpath('//section[@class="index-column"]/ul/li')


    #
    # return articleList

    pages = set()

    def parse_item(self, response):
        item = ArticleItem()
        item['title'] = response.xpath('//h1/text()').extract()
        item['content'] = response.xpath('//article[@class="content-main"]/p//text()').extract()
        commentItem = CommentItem()
        # commentItem['']
        #
        # item['comment'] =
        print(item)
        yield item

    def parse(self, response):
        host = 'http://m.deyi.com'
        articleList = []
        urlList = []
        # print(response.url)
        selList = response.xpath('//section[@class="community-content"]/section')
        # selList = response.xpath('//section[@class="index-column"]/ul/li')
        for i in range(1,10):
            url = ('http://m.deyi.com/forum-41-%d.html') % (i + 1)
            if url not in self.pages:
                self.pages.add(url)
                yield Request(url,dont_filter=True)

        for sel in selList:
            item = ArticleItem()
            # item['title'] = sel.xpath('a/div[@class="left"]/h2/text()').extract()[0]
            # item['desc'] = sel.xpath('a/div[1]/p/text()').extract()[0]
            urlSel = sel.xpath('a/@href')
            if urlSel != None:
                articleUrl = sel.xpath('a/@href').extract()[0]
            item['articleUrl'] = articleUrl
            urlList.append(articleUrl)
            # item['avatar'] = sel.xpath('a//div[@class="info"]/img/@dataimg').extract()[0]
            # item['author'] = sel.xpath('a//span/text()').extract()[0]
            # item['postTime'] = sel.xpath('a//time/text()').extract()[0]
            articleList.append(item)
            urls = urljoin(host,articleUrl)
            if urls not in self.pages:
                self.pages.add(urls)
                yield Request(urls, callback=self.parse_item,dont_filter=True)