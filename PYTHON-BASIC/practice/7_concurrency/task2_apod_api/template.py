API_KEY = "YOUR_KEY"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'


def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> list:
    pass


def download_apod_images(metadata: list):
    pass


def main():
    metadata = get_apod_metadata(
        start_date='2021-08-01',
        end_date='2021-09-30',
        api_key=API_KEY,
    )
    download_apod_images(metadata=metadata)


if __name__ == '__main__':
    main()

### solution ####
import os
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

API_KEY = 'Rb1yezQHrYba9fi5wonkhITeXl1x9jQMYp70o07c'
START_DATE = '2021-08-01'
END_DATE = '2021-09-30'
DOWNLOAD_DIR = 'apod_images'

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def fetch_apod_metadata(start_date, end_date, api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'start_date': start_date,
        'end_date': end_date,
        'thumbs': False
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def download_image(entry):
    if entry['media_type'] != 'image':
        return f"Skipped (not an image): {entry['date']}"
    
    img_url = entry['hdurl'] if 'hdurl' in entry else entry['url']
    img_name = f"{entry['date']}_{os.path.basename(img_url)}"
    img_path = os.path.join(DOWNLOAD_DIR, img_name)

    try:
        img_data = requests.get(img_url, timeout=10)
        img_data.raise_for_status()
        with open(img_path, 'wb') as f:
            f.write(img_data.content)
        return f"Downloaded: {img_name}"
    except Exception as e:
        return f"Failed ({entry['date']}): {e}"

def download_apod_images():
    print("Fetching APOD metadata...")
    entries = fetch_apod_metadata(START_DATE, END_DATE, API_KEY)

    print(f"Found {len(entries)} entries. Starting downloads...")
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(download_image, entry) for entry in entries]
        for future in as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    download_apod_images()
