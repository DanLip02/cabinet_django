import requests

def check_service_status(url, timeout=3):
    try:
        response = requests.head(url, timeout=timeout)
        return response.status_code == 200
    except requests.RequestException:
        return False
