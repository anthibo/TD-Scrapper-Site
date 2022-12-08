import scrapy

class SinglePageSpider(scrapy.Spider):
    name = "single_page_html"
    urls = [
            "https://www.timedoctor.com/integrations-and-addons/",
        ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')