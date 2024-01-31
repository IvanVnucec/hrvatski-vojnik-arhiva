import scrapy


class MagazinesSpider(scrapy.Spider):
    name = "magazines"
    allowed_domains = ["hrvatski-vojnik.hr"]
    start_urls = ["https://hrvatski-vojnik.hr/kategorija/magazin/"]

    def parse(self, response):
        yield from response.follow_all(css="a.next", callback=self.parse)
