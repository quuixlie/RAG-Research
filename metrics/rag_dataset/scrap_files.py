import pandas as pd
import requests
import os
import time

# Read the CSV file containing the dataset
df = pd.read_csv("dataset.csv")

# Drop duplicate URLs to avoid downloading the same file multiple times
unique_files = df[['Book', 'FileNameRelativePath']].drop_duplicates()

# Function to download file with retries
def download_file(url, relative_path, retries=3, backoff_factor=1):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            # Check if the request was successful
            if response.status_code == 200:
                # Ensure the directory exists
                os.makedirs(os.path.dirname(relative_path), exist_ok=True)
                # Save the file to the specified relative path
                with open(relative_path, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded and saved to {relative_path}")
                return  # Exit the function if successful
            else:
                print(f"Failed to download {url}. Status code: {response.status_code}")
                break
        except requests.exceptions.RequestException as e:
            # Handle errors (e.g., network issues)
            print(f"Error downloading {url}: {e}")
        # Retry with backoff
        attempt += 1
        if attempt < retries:
            wait_time = backoff_factor * (2 ** attempt)  # Exponential backoff
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
    print(f"Giving up on {url} after {retries} attempts.")

# Iterate over the unique files and download them one by one
for url, relative_path in zip(unique_files['Book'], unique_files['FileNameRelativePath']):
    print(f"Downloading {url}...")
    download_file(url, relative_path)
