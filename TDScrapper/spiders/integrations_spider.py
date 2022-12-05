import scrapy
import json 

# parsed data schema

# integrations-and-addons page
# (section .intro)
# intro{
#   (h1)
#   header
#   (h2)
#   body
#   }
#
# (section .content)
#   (nav ul .integration-tabs)
#       (li)
#   integration_type {
#           (text) (data-type)
#           code: name
#       }[]
#   (.integrations-list)
#   integration_lists:
#        (a)
#       integration {
#                    (last element of href)
#                   integration_code
#                   view_data: {
#                   (span img)
#                   img -> `id/code`-img // or whatever naming convention
#                   (text of a)
#                   description
#                   (data-type)
#                   integration_type[]
#                               }
#                    intro {
#
#                          }
#                   content {
#
#                           }[]
#
#                   }[]
#


# ${integration} page
#
#


###########
# TODO:
# recursive scrapping
# download images
# pipelines


class IntegrationsSpider(scrapy.Spider):
    name = "integrations"

    def start_requests(self):
        urls = [
            "https://www.timedoctor.com/integrations-and-addons/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # get integration and addons page intro
        intro_path = response.css(".intro")
        intro_header = intro_path.css("h1::text").get()
        intro_body = intro_path.css("h2::text").get()
        intro = {"header": intro_header, "body": intro_body}

        # get integration types
        integration_types_path = response.css(".integration-tabs").css("li")
        integration_types = {}
        for int_type_path in integration_types_path:
            type_code = int_type_path.css("li::attr(data-type)").get()
            type_name = int_type_path.css("a::text").get()
            integration_types[type_code] = type_name

        # get integration
        integrations = []
        integration_lists_path = response.css(".integrations-list").css("a")

        for int_path in integration_lists_path:
            # integration_href= int_path.css("a::href").get()
            # if integration_href == '#' :
            #     integration_href = '/afasd'
            # integration_code = integration_href.split("/")[-2] 
            integration_description = int_path.css("a::text").get()
            integration_type = int_path.css("a::attr(data-type)").get()
            type_name = int_path.css("a::text").get()
            integrations.append({
                'integration_code': 'integration_code',
                'view_data': {
                    'img':'path',
                    'description': integration_description,
                    'integration_type': integration_type
                }
            })
        yield({
            "intro" : intro,
            "integration_type" : integration_types,
            "integrations": integrations,
        })


