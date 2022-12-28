import requests
import pandas as pd

# API endpoints

MCD = "https://www.mcdonalds.com.my/storefinder/index.php"
KFC = "https://kfc.com.my/graphql?query=query+allLocation%7BallLocation%7Blocations%7Baddress+city+code+coleslaw+country+created+curbside+delivery_close+delivery_open+delivery_tier+dinein+drivethru+gesStoreId+is_breakfast+is_delivery+is_selfcollect+lat+launch_date+legacy_store_id+locationId+long+name+phone+riderType+selfcollect_close+selfcollect_open+selfcollect_tier+polygon+smartbox+state+storeCmgId+storeName+updated+zip+disabled_skus+is_breakfast+coleslaw+drivethru+smartbox+dinein+__typename%7D__typename%7D%7D&operationName=allLocation&variables=%7B%7D"
PIZZA_HUT = "https://apiapse1.phdvasia.com/v1/product-hut-fe/localizations"
DOMINOS = "https://order.golo03.dominos.com/store-locator-international/locate/store"

def get_mcd(URL:str = MCD) -> pd.DataFrame:

    payload = dict(
    ajax=1,
    action="get_nearby_stores",
    distance=100000,
    lat='',
    lng='',
    state='',
    products='',
    address='',
    issuggestion=0,
    islocateus=0
    )

    r = requests.post(URL, data=payload)
    data = r.json()["stores"]
    return pd.DataFrame(data)

def get_kfc(URL: str = KFC) -> pd.DataFrame:
    r = requests.get(URL)
    data = r.json()["data"]["allLocation"]["locations"]
    return pd.DataFrame(data)

def get_pizza_hut(URL: str = PIZZA_HUT) -> pd.DataFrame:

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "client": "236e3ed4-3038-441a-be5b-417871eb84d4",
        "lang": "en",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "Referer": "https://www.pizzahut.com.my/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    payload = {
    "limit": 100000000000
    }

    r = requests.get(URL, headers=headers, params=payload).json()

    return pd.DataFrame(r["data"]["items"])

def get_dominos(URL: str = DOMINOS) -> pd.DataFrame:

    headers = {
        "accept": "application/vnd.com.dominos.ecommerce.store-locator.response+json;version=1.2",
        "accept-language": "en-US,en;q=0.9",
        "dpz-language": "en",
        "dpz-market": "MALAYSIA",
        "market": "MALAYSIA",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-dpz-d": "cfea12fe-290a-40fd-aee1-00e3fedba8da",
        "referrer": "https://order.golo03.dominos.com/assets/build/xdomain/proxy.html",
        "referrerPolicy": "strict-origin-when-cross-origin",
        "body": '',
        "method": "GET",
        "mode": "cors",
        "credentials": "omit"
    }

    # east
    lng_e, lat_e = 115.466309,4.740675

    # west
    lng_w, lat_w = 101.975098,4.160158

    payload_e = {
        "latitude": lat_e,
        "longitude": lng_e,
        "g": 1,
        "regionCode": "MY"
    }

    payload_w = {
        "latitude": lat_w,
        "longitude": lng_w,
        "g": 1,
        "regionCode": "MY"
    }

    r_e = requests.get(URL, headers=headers, params=payload_e).json()
    r_w = requests.get(URL, headers=headers, params=payload_w).json()
    r = r_w["Stores"]+r_e["Stores"] 

    return pd.DataFrame(r)