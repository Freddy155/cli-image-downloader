import argparse
import os
import requests

def download_images(urls, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                filename = os.path.join(output_folder, os.path.basename(url))
                with open(filename, "wb") as image_file:
                    image_file.write(response.content)
                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download: {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Image Downloader")
    parser.add_argument("urls", nargs="+", help="List of image URLs")
    parser.add_argument("--output-folder", default="downloaded_images", help="Output folder for downloaded images")
    args = parser.parse_args()

    download_images(args.urls, args.output_folder)

if __name__ == "__main__":
    main()
