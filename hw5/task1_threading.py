import threading
import requests
import json


def validate_url(url, results):
    try:
        response = requests.get(url, timeout=5)
        results.append({
            "url": url,
            "is_ok": response.ok,
            "status_code": response.status_code
        })
    except requests.exceptions.RequestException:
        results.append({
            "url": url,
            "is_ok": False,
            "status_code": None
        })


def main():
    with open("links.txt", "r") as file:
        urls = [line.strip() for line in file.readlines()]

    threads = []
    results = []

    for url in urls:
        thread = threading.Thread(target=validate_url, args=(url, results))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    with open("validated_links.json", "w") as file:
        json.dump(results, file, indent=2)


if __name__ == "__main__":
    main()
