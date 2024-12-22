import scrapy
import requests
import json

class JobSpider(scrapy.Spider):
    name = "job_spider"

    # Start URLs
    start_urls = ['https://www.dice.com/jobs?q=Software&countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=20&filters.postedDate=ONE&filters.workplaceTypes=Remote&filters.employmentType=CONTRACTS&currencyCode=USD&language=en']

    # Headers and Params for API
    headers = {
        'x-api-key': '1YAt0R9wBg4WfsF9VB2778F5CHLAPMVW3WAZcKd8',
    }
    params = {
        'q': 'Software',
        'countryCode2': 'US',
        'radius': '30',
        'radiusUnit': 'mi',
        'page': '1',
        'pageSize': '20',
        'facets': 'employmentType|postedDate|workFromHomeAvailability|workplaceTypes|employerType|easyApply|isRemote|willingToSponsor',
        'filters.workplaceTypes': 'Remote',
        'filters.employmentType': 'CONTRACTS',
        'filters.postedDate': 'ONE',
        'currencyCode': 'USD',
        'fields': 'id|jobId|title|postedDate|jobLocation.displayName|detailsPageUrl|companyName|employmentType|salary',
        'culture': 'en',
        'recommendations': 'true',
        'interactionId': '0',
        'fj': 'true',
        'includeRemote': 'true',
    }

    def start_requests(self):
        # Make the initial request
        yield scrapy.Request(
            url=self.start_urls[0],
            method="GET",
            headers=self.headers,
            callback=self.parse,
            cb_kwargs={"page": 1}
        )

    def parse(self, response, page):
        # Parse JSON response
        data = json.loads(response.body)
        jobs = data.get('data', [])

        for job in jobs:
            yield {
                'id': job.get('id'),
                'jobId': job.get('jobId'),
                'title': job.get('title'),
                'location': job.get('jobLocation', {}).get('displayName'),
                'postedDate': job.get('postedDate'),
                'companyName': job.get('companyName'),
                'employmentType': job.get('employmentType'),
                'salary': job.get('salary'),
                'detailsPageUrl': job.get('detailsPageUrl'),
            }

        # Handle Pagination
        next_page = page + 1
        if data.get('metadata', {}).get('hasNextPage', False):
            self.params['page'] = next_page
            yield scrapy.Request(
                url=self.start_urls[0],
                method="GET",
                headers=self.headers,
                callback=self.parse,
                cb_kwargs={"page": next_page}
            )

        # Send POST Request to Django Backend
        self.send_data_to_backend(jobs)

    def send_data_to_backend(self, jobs):
        url = "http://127.0.0.1:8000/api/jobs/"  # Replace with your Django backend endpoint
        headers = {'Content-Type': 'application/json'}
        for job in jobs:
            payload = json.dumps(job)
            response = requests.post(url, headers=headers, data=payload)
            if response.status_code == 201:
                self.log(f"Job {job['title']} added successfully!")
            else:
                self.log(f"Failed to add job {job['title']}. Response: {response.status_code}")
