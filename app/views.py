from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ScrapedData
from .serializers import ScrapedDataSerializer
import requests
from bs4 import BeautifulSoup

# class ScrapingView(APIView):
#     def get(self, request):
#         # Make a request to the website you want to scrape
#         response = requests.get('https://www.brightermonday.co.ke/jobs')

#         # Parse the HTML content using BeautifulSoup
#         soup = BeautifulSoup(response.content, 'html.parser')

#         # Extract the desired data from the parsed HTML
#         title = soup.find('h1').text
#         content = soup.find('p').text

#         # Create a new ScrapedData instance with the extracted data
#         scraped_data = ScrapedData.objects.create(title=title, content=content)

#         # Serialize the scraped data
#         serializer = ScrapedDataSerializer(scraped_data)

#         return Response(serializer.data)


import requests
from bs4 import BeautifulSoup

def scrape_jobs(request):
    # Send a GET request to the webpage
    url = 'https://www.corporatestaffing.co.ke/jobs/'
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the container that holds the job listings
    job_listings_container = soup.find('main', class_='content')

    # Extract information from each job listing
    job_listings = []
    for job_listing in job_listings_container.find_all('article'):

        # Extract the job title
        title = job_listing.find('h2', class_='entry-title').text.strip()

        # Extract the company name
        time = job_listing.find('p', class_='entry-meta').text.strip()

        # Extract the job description
        description = job_listing.find('div', class_='entry-content').text.strip()

        # Create a dictionary with the extracted information
        job = {
            'title': title,
            'time': time,
            'description': description
        }

        # Add the job to the list
        job_listings.append(job)

    # Return the extracted job information
    return job_listings

# Call the function and store the returned job information
jobs = scrape_jobs(request=scrape_jobs)

# Print the extracted job information
for job in jobs:
    print('Title:', job['title'])
    print('Time:', job['time'])
    print('Description:', job['description'])
    print('---')
