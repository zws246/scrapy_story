import scrapy

from mySpider.mySpider.items import MyspiderItem


class StorySpider(scrapy.Spider):
    # 爬虫名字 启动时使用scrapy crawl + {name}
    name = "story"
    # 作用域
    allowed_domains = ["www.biquger.cc"]
    # 初始页面
    start_urls = ("https://www.biquger.cc/book/889/",)

    def parse(self, response):
        """
        爬虫的主体
        :param response:页面响应内容
        :return: 希望获得的内容
        """
        links = response.xpath('//*[@id="list"]/dl/dd/@href').extract()  # 链接是一个列表
        for i, a in enumerate(links):
            if i > 11:
                url = 'https://www.biquger.cc' + a
                # 回调函数继续执行下一个动作 cb_kwargs 作为回调函数的参数传入
                yield scrapy.Request(url, callback=self.parse_second_step, cb_kwargs={'order': i})

    def parse_second_step(self, response, order):
        """
        下级页面的爬虫主题
        :param response: 页面响应内容
        :return: 需要获得的内容
        """
        item = MyspiderItem()
        item['order'] = order
        # extract 方法拿到的是列表
        item['context'] = "\n".join(response.xpath('//*[@id="content"]/p/text()').extract())
        item['title'] = response.xpath('//*[@id="main"]/div[1]/div/div[2]/h1/text()').extract()[0]
        return item
