import os
import requests


def download_pdfs(links_file: str, output_dir: str):
    """
    Download PDFs from a list of URLs and save them to the specified directory.

    :param links_file: Path to the file containing the list of PDF URLs.
    :param output_dir: Directory where the PDFs will be saved.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read the links from the file
    with open(links_file, "r") as file:
        links = file.readlines()

    # Download each PDF
    for index, link in enumerate(links):
        link = link.strip()  # Remove any leading/trailing whitespace
        if not link:
            continue  # Skip empty lines

        try:
            print(f"Downloading {link}...")
            response = requests.get(link, stream=True)
            response.raise_for_status()  # Raise an error for HTTP issues

            # Extract the filename from the URL
            filename = os.path.basename(link.split("?")[0])
            output_path = os.path.join(output_dir, filename)

            # Save the PDF to the output directory
            with open(output_path, "wb") as pdf_file:
                for chunk in response.iter_content(chunk_size=8192):
                    pdf_file.write(chunk)

            print(f"Saved: {output_path}")
        except Exception as e:
            print(f"Failed to download {link}: {e}")


if __name__ == "__main__":
    # Path to the file containing the PDF links
    links_file = "metrics/pdf_files_links.txt"

    # Directory to save the downloaded PDFs
    output_dir = "dataset"

    # Start downloading
    download_pdfs(links_file, output_dir)
