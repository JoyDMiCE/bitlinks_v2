from dotenv import load_dotenv
import requests
import argparse
import os


def shorten_link(token, link):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {
        "Authorization": "Bearer {}".format(token)
    }
    payload = {
        "long_url": link
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["id"]

def count_clicks(token, link):
    url = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(link)
    headers = {
        "Authorization": "Bearer {}".format(token),
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def main():
    token = os.getenv("BITLY_TOKEN")
    parser = argparse.ArgumentParser(
        description='Сокрощает линки в битлинки, считает клики по битлинкам'
    )
    parser.add_argument('link', help='link, bitlinks')
    args = parser.parse_args()
    print(args.link)
    print(type(args.link))
    try:
        total_clicks = count_clicks(token, args.link)
        print(total_clicks)
    except requests.exceptions.HTTPError:
        bitlink = shorten_link(token, args.link)
        print(bitlink)

if __name__ == "__main__":
    load_dotenv()
    main()
