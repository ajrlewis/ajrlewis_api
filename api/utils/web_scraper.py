import random
from urllib.parse import urlparse
import urllib3
import requests
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers_list = [
    {
        "User-Agent": "Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)"
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3"
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.97 Safari/537.3"
    },
]


def sanitize_url(url: str) -> str:
    url = url.strip()
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = "https://" + url
    if parsed_url.netloc.startswith("www."):
        url = (
            parsed_url.scheme
            + "://"
            + parsed_url.netloc.replace("www.", "", 1)
            + parsed_url.path
        )
        if parsed_url.query:
            url += f"?{parsed_url.query}"
    return url


def get_response(url: str) -> requests.models.Response:
    headers = random.choice(headers_list)
    sanitized_url = sanitize_url(url)
    print("url = ", url)
    print("sanitized_url = ", sanitized_url)
    response = requests.get(
        sanitized_url, headers=headers, allow_redirects=True, timeout=20
    )
    response.raise_for_status()
    return response


def check_website_exists(url: str) -> bool:
    try:
        response = get_response(url)
        return True
    except requests.exceptions.RequestException:
        return False


def scrape_website_for_text(url: str) -> tuple[str, str]:
    print(f"{__name__}.scrape_website_for_text")
    try:
        response = get_response(url)
    except requests.exceptions.RequestException as e:
        # text, error = scrape_dynamic_website_for_text(url)
        text, error = search_bing(url)
        if text:
            return text, ""
        return "", f"{e}. {error}"
    # print(f"{__name__}.scrape_website_for_text", "response = ", response)
    # print(f"{__name__}.scrape_website_for_text", "response.text = ", response.text)
    # print(
    #     f"{__name__}.scrape_website_for_text", "response.content = ", response.content
    # )
    content_type = response.headers.get("content-type", "")
    # print(f"{__name__}.scrape_website_for_text", "content_type = ", content_type)
    response_is_xml = "xml" in content_type
    if response_is_xml:
        parser = "lxml-xml"
        markup = response.content
    else:
        parser = "html.parser"
        markup = response.text
    text = ""
    try:
        soup = BeautifulSoup(markup, parser)
        if response_is_xml:
            texts = []
            items = soup.find_all("item")
            for item in items:
                title = item.find("title").text.strip()
                description = item.find("description").text.strip()
                texts.append(f"{title}: {description}")
            text = "\n".join(texts)
        else:
            text = soup.body.get_text(" ", strip=True)
    except Exception as e:
        return "", f"BeautifulSoup unable to extract body from response text {e}."
    # print(f"{__name__}.scrape_website_for_text", "text = ", text, not text)
    if not text:
        # text, error = scrape_dynamic_website_for_text(url)
        text, error = search_bing(url)
        if text:
            return text, ""
    return text, ""


def search_bing(query: str):
    url = f"https://www.bing.com/search?q={query}&count=1"
    print(f"{__name__}.search_bing", "url = ", url)
    text, error = scrape_website_for_text(url)
    return text, error


# def scrape_dynamic_website_for_text(url: str) -> tuple[str]:
#     print(f"{__name__}.scrape_dynamic_website_for_text")

#     import os
#     import time

#     # from seleniumwire import webdriver
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.chrome.service import Service as ChromeService
#     from webdriver_manager.chrome import ChromeDriverManager

#     chrome_options = webdriver.ChromeOptions()
#     # chrome_options.add_argument("--headless=new")
#     # chrome_options.add_argument("--ignore-certificate-errors")
#     # chrome_options.add_argument("--no-sandbox")
#     # chrome_options.add_argument("disable-notifications")
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--window-size=1280x1696")
#     chrome_options.add_argument("--user-data-dir=/tmp/user-data")
#     chrome_options.add_argument("--hide-scrollbars")
#     chrome_options.add_argument("--enable-logging")
#     chrome_options.add_argument("--log-level=0")
#     chrome_options.add_argument("--v=99")
#     chrome_options.add_argument("--single-process")
#     chrome_options.add_argument("--data-path=/tmp/data-path")
#     chrome_options.add_argument("--ignore-certificate-errors")
#     chrome_options.add_argument("--homedir=/tmp")
#     chrome_options.add_argument("--disk-cache-dir=/tmp/cache-dir")
#     chrome_options.add_argument(
#         "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
#     )
#     chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

#     driver = webdriver.Chrome(options=chrome_options)

#     # driver = webdriver.Chrome(
#     #     service=ChromeService(ChromeDriverManager(driver_version="2.26").install()),
#     #     options=chrome_options,
#     #     seleniumwire_options={"request_storage_base_dir": "/tmp"},
#     # )

#     # from seleniumwire import webdriver
#     # from selenium.webdriver.chrome.service import Service
#     # from webdriver_manager.chrome import ChromeDriverManager
#     # from selenium.webdriver.chrome.options import Options

#     # chrome_options = Options()
#     # chrome_options.add_argument("--headless")
#     # chrome_options.add_argument("--no-sandbox")
#     # chrome_options.add_argument("--start-maximized")
#     # chrome_options.add_argument("--start-fullscreen")
#     # chrome_options.add_argument("--single-process")
#     # chrome_options.add_argument("--disable-dev-shm-usage")
#     # chrome_options.add_argument("--disk-cache-size-0")

#     # driver = webdriver.Chrome(
#     #     options=chrome_options,
#     #     service=Service(ChromeDriverManager().install()),
#     #     seleniumwire_options={"request_storage_base_dir": "/tmp"},
#     # )

#     driver.get(url)

#     texts = []
#     elements = driver.find_elements(By.TAG_NAME, "p")
#     for element in elements:
#         text = element.text
#         if text:
#             texts.append(text)
#     text = " ".join(texts)
#     error = "" if text else "Failed to scrape dynamic website for text."
#     return text, error


def main():
    url = "https://gameswift.io/"
    # url = "https://www.coindesk.com/arc/outboundfeeds/rss/"
    text, error = scrape_website_for_text(url)
    # query = "https://Hyperhumans.ai"
    # query = "ajrlewis.com"
    # query = "who is the president of the us"
    # text, error = search_bing(query)
    print(f"{text = }")
    print(f"{error = }")


if __name__ == "__main__":
    main()
