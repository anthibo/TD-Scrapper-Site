import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class IntegrationsHTMLSpiderAll(CrawlSpider):
    name = 'all'

    allowed_domains = ['www.timedoctor.com', 'site.timedoctor.com']
    start_urls = ['https://www.timedoctor.com/']

    custom_settings = {
        'LOG_LEVEL': 'INFO'
    }

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print('Downloaded... ', response.url)
        filename = f'pages/{response.url.split("/")[-1]}.html'
        print('Saving as :', filename)
        with open(filename, 'wb') as f:
            # print(response.body)
            f.write(response.body)
