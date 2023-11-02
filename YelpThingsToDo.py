import requests
from bs4 import BeautifulSoup
import csv

response = requests.get('https://www.yelp.com/search?find_desc=Fun+Things+To+Do&find_loc=New+York%2C+NY')

soup = BeautifulSoup(response.content, 'html.parser')

activities = soup.find_all('a', class_='css-19v1rkv')
ratings = soup.find_all('span', class_='css-gutk1c')
reviews = soup.find_all('span', class_='css-8xcil9')

file_name = 'YelpActivities.csv'

with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:  # Specify the encoding as utf-8
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(['Activity', 'Rating', 'Review Count'])

    for activity, rating, review in zip(activities, ratings, reviews):
        activity_text = activity.get_text(strip=True)
        rating_text = rating.get_text(strip=True)
        review_text = review.get_text(strip=True)

        # Check if the rating text contains unwanted phrases and exclude them
        if "Yelp for Business" in rating_text or "Bird's-eye View" in rating_text:
            continue  # Skip this entry

        csvwriter.writerow([activity_text, rating_text, review_text])
