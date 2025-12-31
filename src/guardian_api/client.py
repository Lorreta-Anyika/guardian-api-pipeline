import logging
import os

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

api_key = os.getenv("GUARDIAN_API_KEY")

base_url = "https://content.guardianapis.com/search"


def fetch_data(
        query, 
        page_size=20, 
        start_date="2025-11-15", 
        stop_date="2025-11-24",
    ):
    """
    Fetch paginated articles from the Guardian API.

    This function sends repeated GET requests to the Guardian Content API,
    handling pagination automatically. Each page of results is appended
    to the QUERY_CONTAINER list. The function uses the PARAMETERS
    dictionary for query configuration and logs each page fetched.
    """
    query_container = []

    parameters = {
        "api-key": api_key,
        "q": query,
        "page-size": page_size,
        "order-by": "newest",
        "from-date": start_date,
        "to-date": stop_date,
    }
    current_page = 1
    total_pages = 1

    while current_page <= total_pages:
        response = requests.get(base_url, params=parameters)

        if response.status_code != 200:
            response.raise_for_status()

        data = response.json()

        for article in data["response"]["results"]:
            query_container.append(article)

        logging.info(f"Fetched page {current_page}/ {total_pages}")

        total_pages = data["response"]["pages"]
        current_page += 1

    return query_container
