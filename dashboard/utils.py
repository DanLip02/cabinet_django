import requests
from requests.auth import HTTPBasicAuth
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def print_dom_structure(html: str, max_depth=3, indent=2):
    def recurse(element, depth=0):
        if depth > max_depth:
            return
        if hasattr(element, "name") and element.name is not None:
            print(" " * (depth * indent) + f"<{element.name}>")
            for child in element.children:
                recurse(child, depth + 1)

    soup = BeautifulSoup(html, "html.parser")
    recurse(soup.body or soup, 0)

def check_service_status(config, timeout=10):
    url = config["url"]
    auth = config.get("auth")
    service_type = config.get("type", "basic")

    try:
            http_auth = HTTPBasicAuth(*auth) if auth else None

            if isinstance(http_auth, HTTPBasicAuth):
                username = http_auth.username
                print("Auth username:", username)
            else:
                print("No auth or not HTTPBasicAuth")

            response = requests.get(url, timeout=timeout, auth=http_auth, verify=False)

            if response.status_code != 200:
                print(f"Сервис {url} ответил кодом {response.status_code}")
                return False

            return True
            # return response.status_code == 200

    except requests.RequestException as e:
        print(f"Ошибка при проверке сервиса {url}: {e}")
        return False
