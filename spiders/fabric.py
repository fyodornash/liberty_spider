# -*- coding: utf-8 -*-
import scrapy
import logging


class FabricSpider(scrapy.Spider):
    name = 'fabric'
    start_urls = ['http://www.libertylondon.com/uk/department/fabric/cotton-tana-lawn/', 'http://www.libertylondon.com/uk/department/fabric/silk/', 'http://www.libertylondon.com/uk/department/fabric/wool/', 'http://www.libertylondon.com/uk/department/fabric/poplin/', 'http://www.libertylondon.com/uk/department/fabric/viscose-jersey/', 'http://www.libertylondon.com/uk/department/fabric/furnishing-fabric/',
    'https://www.libertylondon.com/uk/department/fabric/furnishing-fabric/?sz=60&start=60',
    'https://www.libertylondon.com/uk/department/fabric/cotton-tana-lawn/?sz=60&start=60',
    'https://www.libertylondon.com/uk/department/fabric/cotton-tana-lawn/?sz=60&start=120',
    'https://www.libertylondon.com/uk/department/fabric/cotton-tana-lawn/?sz=60&start=180',
    'https://www.libertylondon.com/uk/department/fabric/cotton-tana-lawn/?sz=60&start=240',
    'https://www.libertylondon.com/uk/department/fabric/cotton-tana-lawn/?sz=60&start=300',
    'https://www.libertylondon.com/uk/department/fabric/cotton-tana-lawn/?sz=60&start=360',
    'https://www.libertylondon.com/uk/department/fabric/silk/?sz=60&start=60',
    'https://www.libertylondon.com/uk/department/fabric/silk/?sz=60&start=120',
    'https://www.libertylondon.com/uk/department/fabric/silk/?sz=60&start=180',
    'https://www.libertylondon.com/uk/department/fabric/silk/?sz=60&start=240',
]

    def parse(self, response):
        images = response.xpath('//div[@class="product-image"]/a/img[not(@class="alt-img")]/@data-src').extract()
        titles = response.xpath('//div[@class="product-image"]/a/img[not(@class="alt-img")]/@title').extract()
        urls = response.xpath('//div[@class="product-image"]/a/img[not(@class="alt-img")]/@data-src').extract()
        for image,title, url in zip(images,titles, urls):

            yield{
                'title': title,
                'image_urls': [image],
                'url': url,
            }
            
            
        next_page = response.xpath('//div[@class="liberty-london-crest infinite-scroll-placeholder"]/a/@data-grid-url').extract_first()
        if next_page is not None:
            np = next_page.replace('amp;', '').split('format')[0]
            logging.info(np)
            yield response.follow(np, self.parse)
                    
