import scrapy

class IntegrationsHTMLSpider(scrapy.Spider):
    name = "integrations_html"
    urls = [
            "https://www.timedoctor.com/integrations-and-addons/",
        ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        # self.urls.append()
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')