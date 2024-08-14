import scrapy


class Database(scrapy.Item):
    draw_date = scrapy.Field()
    lottery_numbers = scrapy.Field()
    raffle_stars = scrapy.Field()