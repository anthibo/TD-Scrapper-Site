import scrapy

class IntegrationsHTMLSpider(scrapy.Spider):
    name = "integrations_static_html"
    url = "https://www.timedoctor.com/integrations-and-addons/"
    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)



    def parse(self, response):
        self.write_html_page(response=response)
        integration_links = response.css(".integrations-list").css("a::attr(href)").getall()
        for integration_link in integration_links:

            if integration_link is not "#":
                yield scrapy.Request(url=integration_link, callback=self.write_html_page)
    
    def write_html_page(self, response):
        print('response.url search me')
    
        print(response.url)
        page = response.url.split("/")[-1]
        print('page search me')
        print(page)
        filename = f'{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')