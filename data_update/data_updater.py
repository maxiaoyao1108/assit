import time
from data_collection import market_data_collector, economic_data_collector, news_collector
from data_processing import data_cleaner, data_storer


def data_update():
    while True:
        market_data = market_data_collector.collect_market_data()
        economic_data = economic_data_collector.collect_economic_data()
        news_data = news_collector.collect_news_data()

        cleaned_market_data = data_cleaner.clean_data(market_data)
        cleaned_economic_data = data_cleaner.clean_data(economic_data)
        cleaned_news_data = data_cleaner.clean_data(news_data)

        data_storer.store_data(cleaned_market_data, 'market_data')
        data_storer.store_data(cleaned_economic_data, 'economic_data')
        data_storer.store_data(cleaned_news_data, 'news_data')

        print("数据更新完成，等待下一次更新...")
        time.sleep(3600)  # 每小时更新一次

    