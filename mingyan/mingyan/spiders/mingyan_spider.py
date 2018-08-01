import scrapy

class mingyan(scrapy.Spider): #需要继承scrapy.Spider类
    name = "mingyan"  # 定义蜘蛛名

    # # ---------------------------------------------scrapy初始url方法一-----------------------------------------
    # def start_requests(self):
    #     urls = ['http://lab.scrapyd.cn/page/1/', 'http://lab.scrapyd.cn/page/2/']
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)  #爬取到的页面如何处理？提交给parse方法处理
    # # ----------------------------------------------------------------------------------------------------------

    # # ---------------------------------------------scrapy初始url方法二-----------------------------------------
    # 方法二，无需定义start_requests方法
    start_urls = [
        "http://lab.scrapyd.cn/page/1/",
        "http://lab.scrapyd.cn/page/2/",
    ]
    # # ----------------------------------------------------------------------------------------------------------

    def parse(self, response):
        # response: <200 url>
        # response.body   整个url的html
        mingyan = response.css('div.quote')
        for v in mingyan:
            text = v.css('.text::text').extract_first()  # 提取名言
            autor = v.css('.author::text').extract_first()  # 提取作者
            tags = v.css('.tags .tag::text').extract()  # 提取标签
            tags = ','.join(tags)  # 数组转换为字符串

            fileName = '%s-语录.txt' % autor
            with open(fileName, "a+", encoding="utf-8") as f:  # 不同人的名言保存在不同的txt文档，“a+”以追加的形式
                f.write(text)
                f.write('\n')  # ‘\n’ 表示换行
                f.write('标签：' + tags)
                f.write('\n-------\n')
                f.close()
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)





