import locale
from datetime import datetime
from Database.Connection_Mongodb import MongodbDatabase


class EuroMillionPipeline():

    def process_item(self, item, spider):
        item["lottery_numbers"] = [int(num) for num in item["lottery_numbers"]]
        item["raffle_stars"] = [int(num) for num in item["raffle_stars"]]

        self.process_date(item=item)

        return item
    
    def process_date(self, item):
        locale.setlocale(locale.LC_TIME, 'pt_PT.UTF-8')
        day_of_week = item["draw_date"].split()[0]
        date = " ".join(item["draw_date"].split()[1:])
        format_date = datetime.strptime(date, "%d de %B de %Y").strftime("%d/%m/%Y")
        
        item.pop('draw_date', None)
        item["day_of_week"] = day_of_week
        item["day"] = int(format_date.split("/")[0])
        item["month"] = int(format_date.split("/")[1])
        item["year"] = int(format_date.split("/")[2])


        self.insert_data(item)

        return item

    def insert_data(self, item):
        connection = MongodbDatabase().connect_mongo()
        collection = MongodbDatabase().collection_create(connection)
        
        collection.insert_one(dict(item))

        return item