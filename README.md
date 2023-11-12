# CLI-Image-Downloader

## Introduction

This documentation provides a detailed explanation of the `cli-image-downloader` Python script, which is used for downloading images from a list of URLs. The script utilizes the `argparse`, `os`, and `requests` libraries to facilitate this functionality.

## Table of Contents

1\. [Overview](#overview)

2\. [Prerequisites](#prerequisites)

3\. [Usage](#usage)

   - [Command Line Arguments](#command-line-arguments)

4\. [Functionality](#functionality)

5\. [Examples](#examples)

## Overview <a name="overview"></a>

The `cli-image-downloader` script is a Python program designed to enable users to download images from a list of URLs. It accepts a list of image URLs as input and saves the downloaded images to a specified output folder. This script is particularly useful for batch downloading images from the internet.

## Prerequisites <a name="prerequisites"></a>

Before using the `cli-image-downloader` script, make sure you have the following prerequisites:

- Python installed on your system.

- The `argparse`, `os`, and `requests` libraries installed. You can install these libraries using pip:

```shell

pip install argparse os requests

```

## Usage <a name="usage"></a>

To utilize the `cli-image-downloader` script, follow these steps:

1\. Open your terminal or command prompt.

2\. Navigate to the directory where `app.py` is located.

3\. Run the script with the following command:

```shell

python app.py [URLs] [--output-folder OUTPUT_FOLDER]

```

### Command Line Arguments <a name="command-line-arguments"></a>

- `[URLs]`: One or more space-separated URLs of the images you wish to download.

- `--output-folder OUTPUT_FOLDER`: (Optional) The output folder where the downloaded images will be saved. If not provided, the default folder is "downloaded_images."

## Functionality <a name="functionality"></a>

The `cli-image-downloader` script primarily consists of the following functions:

1\. `download_images(urls, output_folder)`: This function downloads images from a list of URLs and saves them to the specified output folder. If the output folder does not exist, it will be created.

2\. `main()`: This is the main function that parses command-line arguments using argparse and calls the `download_images` function with the provided URLs and output folder.

## Examples <a name="examples"></a>

Here are some examples of how to use the `cli-image-downloader` script:

### Example 1: Downloading Images to the Default Folder

```shell

python app.py https://example.com/image1.jpg https://example.com/image2.jpg

```

This command will download the images from the specified URLs and save them in the "downloaded_images" folder.

### Example 2: Downloading Images to a Custom Folder

```shell

python app.py https://example.com/image3.jpg https://example.com/image4.jpg --output-folder custom_folder

```

This command will download the images from the specified URLs and save them in the "custom_folder" folder.

That's it! You now have a clear understanding of how to use the `cli-image-downloader` script to download images from URLs. Feel free to explore its functionality further to suit your needs.