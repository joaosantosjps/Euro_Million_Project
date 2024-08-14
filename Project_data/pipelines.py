from Data.items import Database


class ProcessNumbersPipeline:
    def process_item(self, item, spider):
        print(spider)
        return item
