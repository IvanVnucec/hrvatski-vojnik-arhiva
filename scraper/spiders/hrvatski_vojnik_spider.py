import scrapy


class HrvatskiVojnikSpider(scrapy.Spider):
    name = "hrvatski_vojnik"
    allowed_domains = ["hrvatski-vojnik.hr"]
    start_urls = ["https://hrvatski-vojnik.hr/kategorija/magazin/"]

    def parse(self, response):
        title_hrefs = response.css("h3.article-preview__title a::attr(href)").getall()
        filtered = filter(lambda href: href.startswith("https://hrvatski-vojnik.hr/kategorija/magazin/"), title_hrefs)
        yield from response.follow_all(filtered, self.parse_article)
        yield from response.follow_all(css="a.next", callback=self.parse)

    def parse_article(self, response):
        yield {
            "file_urls": response.css("a.btn--download-magazin::attr(href)").get(),
        }
