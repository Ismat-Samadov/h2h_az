import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class MainSpider(CrawlSpider):
    name            = 'main'
    allowed_domains = ['h2h.az']
    start_urls      = ['https://h2h.az/elanlar']

    rules = (
               Rule(LinkExtractor( allow    =  ('/item/')),
                                   callback =  'parse_item',
                                   follow   =  True
                   ),
            )

    def parse_item(self, response):
        self.logger.info('Parsing page: %s', response.url)
        yield {
            'url'         : response.url,
            'phone'       : response.css('.item-person-detail a[href^="tel:"]::text').get(),
            'name'        : response.css('.item-person-detail div[style="padding:5px 0"]::text').get(),
            'p_type'      : response.css('.item-person-detail div.personType::text').get(),

        }
