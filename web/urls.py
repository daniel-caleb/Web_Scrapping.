from django.urls import path
from app.views import scrape_jobs

urlpatterns = [
    path('api/scrape/', scrape_jobs, name='scraping-jobs'),
]
