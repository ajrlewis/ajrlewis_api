import urllib3
import requests
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_response(url: str) -> requests.models.Response:
    headers = {
        "User-Agent": "Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)"
    }

    response = requests.get(
        url, headers=headers, verify=False, allow_redirects=True, timeout=20
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
    try:
        response = get_response(url)
    except requests.exceptions.RequestException as e:
        return "", f"{e}"
    try:
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.body.get_text(" ", strip=True)
    except AttributeError as e:
        return "", "BeautifulSoup unable to extract body from response text."
    return text, ""
