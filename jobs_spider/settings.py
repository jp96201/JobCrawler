# Scrapy settings for jobs_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jobs_spider'

SPIDER_MODULES = ['jobs_spider.spiders']
NEWSPIDER_MODULE = 'jobs_spider.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

SPIDER_MIDDLEWARES = {
    'scrapy_deltafetch.DeltaFetch': 100,
    'scrapy_magicfields.MagicFieldsMiddleware': 200,
}

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"

DELTAFETCH_ENABLED = True

MAGICFIELDS_ENABLED = True
MAGIC_FIELDS = {
    "timestamp": "$time",
    "spider": "$spider:name",
    "url": "scraped from $response:url",
    "domain": "$response:url,r'https?://([\w\.]+)/']",
}

ITEM_PIPELINES = {
    'jobs_spider.pipelines.JobsSpiderPipeline': 300,
    'jobs_spider.pipelines.JsonWriterPipeline': 800,
}

