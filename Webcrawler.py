import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import random

# User-Agents (replace with your actual list)
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
    # Add more user agents here
]

def webcrawler(url, max_pages=1):
    """A web crawler with a fancy header and user-agent rotation."""

    visited_links = set()

    print(r"""
    ******************************************
    *  _   _      _ _         _     _        *
    * | | | | ___| | | ___   | |   (_) ___   *
    * | |_| |/ _ \ | |/ _ \  | |   | |/ __|  *
    * |  _  |  __/ | | (_) | | |___| | (__   *
    * |_| |_|\___|_|_|\___/  |_____|_|\___|  *
    *                                        *
    *          Web Crawler in Action         *
    ******************************************
    """)

    for page in range(1, max_pages + 1):
        print(f"Scraping page {page}...")
        try:
            # Choose a random user agent
            headers = {'User-Agent': random.choice(user_agents)}

            response = requests.get(url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract links and process them (replace with your desired logic)
            links = []
            for link_element in soup.find_all('a'):
                href = link_element.get('href')
                if href:
                    links.append(urljoin(url, href))

            for link in links:
                if link not in visited_links:
                    visited_links.add(link)
                    print(f"Processing: {link}")
                    # Add your logic here to process each link

        except requests.exceptions.RequestException as e:
            print(f"Error scraping page {page}: {e}")


if __name__ == "__main__":
    url = input("Enter the URL to crawl: ")
    max_pages = int(input("How many pages do you want to crawl? "))

    webcrawler(url, max_pages)
