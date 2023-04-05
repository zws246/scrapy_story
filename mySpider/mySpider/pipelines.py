# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyspiderPipeline:
    """执行数据存储的过程 """

    def open_scrapy(self, spider):  # 首先定义一个列表
        self.items = []

    def process_item(self, item, spider):  # 数据通过过程放入到一个列表中
        self.items.append(item)
        return item

    def close_scrapy(self, spider):  # 结束时对列表进行排序并执行保存
        with open('深空彼岸.txt', 'a+', encoding='utf-8') as f:
            self.items.sort(key=lambda i: i['order'])  # 通过Key的值排序
            for item in self.items:
                f.write(item['title'])
                f.write('\n')
                f.write(item['context'])
                f.write()
