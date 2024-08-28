import scrapy
from Project_data.items import Database


class EuroMillionSpider(scrapy.Spider):
    name = "euro_million"
    allowed_domains = ["www.euro-millions.com"]
    start_urls = "https://www.euro-millions.com/pt/resultados"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com/'
    }

    def start_requests(self):

        yield scrapy.Request(
            url=self.start_urls,
            headers=self.headers,
            callback=self.parse
            )
        
    def parse(self, response):
        list_yaers_links = response.xpath('//*[@id="content"]/div[3]/div/div/div/ul/li/a/@href').extract()
        
        for years_link in list_yaers_links:
            
            yield scrapy.Request(
                url=f"https://{self.allowed_domains[0]}{years_link}",
                headers=self.headers,
                callback=self.get_date
            )
    
    def get_date(self, response):        
        list_dates_links = response.xpath('//*[@id="resultsTable"]/tbody/tr[@class="resultRow"]/td[@class="date noBefore"]/a/@href').extract()
        
        for date_link in list_dates_links:
            
            yield scrapy.Request(
                url=f"https://{self.allowed_domains[0]}{date_link}", 
                headers=self.headers,
                callback=self.get_numbers       
            )
    
    def get_numbers(self, response):
        path = response.xpath('//*[@id="content"]/div[@class="fx btwn wrapSM"]/div[@class="box half fx col jcen"]')
        
        draw_date = path.xpath('//div/div[@class="h3"]/text()').extract_first()
        lottery_numbers = path.xpath('//div/ul[@id="ballsAscending"]/li[@class="resultBall ball"]/text()').extract()
        raffle_stars = path.xpath('//div/ul[@id="ballsAscending"]/li[@class="resultBall lucky-star"]/text()').extract()
        draw_numbers = response.xpath('/html/head/meta[@name="description"]/@content').extract_first().split(":")[1].replace(".", " ")

        yield Database(
            {
            "draw_date": draw_date,
            "lottery_numbers": lottery_numbers,
            "raffle_stars": raffle_stars,
            "draw_numbers": draw_numbers
        })
    