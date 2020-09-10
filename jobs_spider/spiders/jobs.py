import scrapy

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['zhipin.com']
    cookie={'Cookie': '__zp_seo_uuid__=df273407-d5ca-455c-a238-d51daf7c24a7; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1598340681,1598776817,1598777732; lastCity=101010100; __zp_stoken__=de83bfFEkE3tKfx9JcVNJA3Q4H2krWgp5JH4lKCtpGgJXUR0ZZUwwSEI9QSkrcwERHntwZCQ%2Feih2IDYdeUNqRDgXIS5qTn8HQzJsBjZfOF4kOXZcBhxJE1JRND42ExBoGCoNAmREYFZdXAl%2BfA%3D%3D; __c=1598340680; __l=l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3D&r=https%3A%2F%2Fwww.google.com%2F&g=&friend_source=0&friend_source=0; __a=88942536.1598340680..1598340680.37.1.37.37; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1598875267'}
    query = ''
    city = '101210100'
    industry = ''
    position = '100999'
    start_urls = [
        'https://www.zhipin.com/job_detail/?query='+query+'&city='+city+'&industry='+industry+'&position='+position,
    ]

    def parse(self, response):
        for job_url in response.xpath('//div[@class="job-primary"]//div[@class="primary-box"]/@href').getall():
            yield scrapy.Request(response.urljoin(job_url), cookies=self.cookie, callback=self.parse_job_page)
        next_page = response.xpath('//a[@ka="page-next"]').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), cookies=self.cookie ,callback=self.parse)

    def parse_job_page(self, response):
        item = {}

        job_banner = response.xpath('//div[@class="job-banner"]')
        job_detail = response.xpath('//div[@class="job-detail"]')

        item["status"] = job_banner.xpath('//div[@class="job-status"]//span/text()').get()
        item["title"] = job_banner.xpath('//div[@class="name"]//h1/text()').get()
        item["salary"] = job_banner.xpath('//div[@class="name"]//*[@class="salary"]/text()').get()
        item["city"] = job_banner.xpath('//*[@class="text-city"]/text()').get()
        item["exp"] = job_banner.xpath('//*[@class="dolt"][1]/following-sibling::text()[1]').get()
        item["degree"] = job_banner.xpath('//*[@class="dolt"][2]/following-sibling::text()[1]').get()
        item['description'] = job_detail.xpath(
            '//div[@class="job-sec"]//div[@class="text"]/text()'
        ).getall()

        yield item

