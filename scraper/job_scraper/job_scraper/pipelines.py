import requests

class JobScraperPipeline:
    def process_item(self, item, spider):
        try:
            response = requests.post('http://localhost:8000/api/jobs/', json=item)
            spider.logger.info(f"Job posted: {item['title']}")
        except Exception as e:
            spider.logger.error(f"Failed to post job: {e}")
        return item
