import random
from urllib.parse import urlparse
import urllib3
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers_list = [
    {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    },
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


def get_random_headers() -> dict:
    return random.choice(headers_list)


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
    headers = get_random_headers()
    sanitized_url = sanitize_url(url)
    response = requests.get(
        sanitized_url, headers=headers, verify=True, allow_redirects=True, timeout=20
    )
    response.raise_for_status()
    return response


def check_website_exists(url: str) -> bool:
    try:
        _ = get_response(url)
        return True
    except requests.exceptions.RequestException:
        return False


def scrape_website_for_text(url: str) -> tuple[str, str]:
    print(f"{__name__}.scrape_website_for_text", "url = ", url)
    try:
        response = get_response(url)
    except requests.exceptions.RequestException as e:
        print(f"{__name__}.scrape_website_for_text", "Failed to get response", e)
        text, error = scrape_dynamic_website_for_text(url)
        if text:
            return text, ""
        return "", f"{e}. {error}"
    content_type = response.headers.get("content-type", "")
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

    if not text:
        print(f"{__name__}.scrape_website_for_text", "text = ", text)
        text, error = scrape_dynamic_website_for_text(url)
        if text:
            return text, ""
        return "", f"{error}"

    return text, ""


def scrape_dynamic_website_for_text(url: str) -> tuple[str]:
    print(f"{__name__}.scrape_dynamic_website_for_text")

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1280x1696")
    # chrome_options.add_argument("--user-data-dir=/tmp/user-data")
    # chrome_options.add_argument("--hide-scrollbars")
    # chrome_options.add_argument("--enable-logging")
    # chrome_options.add_argument("--log-level=0")
    # chrome_options.add_argument("--v=99")
    # chrome_options.add_argument("--single-process")
    # chrome_options.add_argument("--data-path=/tmp/data-path")
    # chrome_options.add_argument("--ignore-certificate-errors")
    # chrome_options.add_argument("--homedir=/tmp")
    # chrome_options.add_argument("--disk-cache-dir=/tmp/cache-dir")
    # headers = get_random_headers()
    # chrome_options.add_argument(f"user-agent={headers['User-Agent']}")
    # driver = webdriver.Chrome(options=chrome_options)

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-gpu")
    firefox_options.add_argument("--window-size=1280x1696")
    firefox_options.add_argument("--user-data-dir=/tmp/user-data")
    firefox_options.add_argument("--hide-scrollbars")
    firefox_options.add_argument("--enable-logging")
    firefox_options.add_argument("--log-level=0")
    firefox_options.add_argument("--v=99")
    firefox_options.add_argument("--single-process")
    firefox_options.add_argument("--data-path=/tmp/data-path")
    firefox_options.add_argument("--ignore-certificate-errors")
    firefox_options.add_argument("--homedir=/tmp")
    firefox_options.add_argument("--disk-cache-dir=/tmp/cache-dir")
    headers = get_random_headers()
    firefox_options.add_argument(f"user-agent={headers['User-Agent']}")
    print(
        f"{__name__}.scrape_dynamic_website_for_text",
        "firefox_options = ",
        firefox_options,
    )
    driver = webdriver.Firefox(options=firefox_options)
    print(f"{__name__}.scrape_dynamic_website_for_text", "driver = ", driver)
    driver.get(url)

    # driver.get(url)

    texts = []
    elements = driver.find_elements(By.TAG_NAME, "p")
    for element in elements:
        text = element.text
        if text:
            texts.append(text)
    text = " ".join(texts)
    error = "" if text else "Failed to scrape dynamic website for text."
    return text, error


def search_bing(query: str) -> tuple[str]:
    url = f"https://www.bing.com/search?q={query}&count=1"
    print(f"{__name__}.search_bing", "url = ", url)
    text, error = scrape_website_for_text(url)
    return text, error


def main():
    # url = "https://gameswift.io/"
    # url = "https://www.coindesk.com/arc/outboundfeeds/rss/"
    text, error = scrape_website_for_text(url)
    # query = "who is the president of the us"
    # text, error = search_bing(query)
    print(f"{text = }")
    print(f"{error = }")


if __name__ == "__main__":
    main()
