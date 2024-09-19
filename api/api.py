
import requests

# from service.teem_service import convert_to_


def get_data_api(url : str):
    try:
        response = requests.get(url)  # Timeout in seconds
        response.raise_for_status()
        return response.json()# Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print('Request failed:', e)

def get_season(n : int):
    users_url = f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={n}&&pageSize=1000"
    return get_data_api(users_url)


