from datetime import datetime

from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm
class ScrapingFailedError(Exception):
    ...

"""
pass, ... (ellipsis)
"""

def scrape(page_number: int):
    url_to_scrape = f"https://telegrafi.com/lajme/page/{page_number}"

    response = requests.get(url_to_scrape)

    if response.status_code != 200:
        raise ScrapingFailedError

    html_text = response.text

    soup = BeautifulSoup(html_text, "html.parser")

    main_div = soup.find("div", class_="catgory-latest category-page--listing")

    articles = main_div.find_all("a", class_="post__large")

    results = []
    for article in tqdm(articles):
        news_name = article.get('data-vr-contentbox', "Name Not Available")

        news_link = article.get("href", "Link Not Available")

        image = article.find("img")
        image_link = image.get("src", "Image Link Not Available")

        post_date_info = article.find('div', class_='post_date_info').text
        post_date_info = post_date_info.lstrip("|").lstrip()



        news_category = article.find("div", class_="post__large--details").text

        results.append(
            {
                "name": news_name,
                "news_url": news_link,
                "image_url": image_link,
                "date_scraped": datetime.now(),
                "post_date_info": post_date_info,
                "news_category": news_category,
            }
        )
    return results

number_of_pages = 1

final_results = []
for page in range(1, number_of_pages+1):
    temp_results = scrape(page)
    final_results.extend(temp_results)

results_df = pd.DataFrame(final_results)
results_df.to_csv("telegrafi_data.csv")

