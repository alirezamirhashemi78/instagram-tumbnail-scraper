from bs4 import BeautifulSoup
import os


def retrieve_image_url(soup):
    # Finds the thumbnail image URL from the Instagram page soup.
    image_meta = soup.find("meta", property="og:image")
    if not image_meta:
        print("Thumbnail image not found.")
        return None
    return image_meta["content"]


def download_image(conn, img_url):
    # Downloads the image content using the Connection object.
    try:
        response = conn.get(img_url)
        if response and response.status_code == 200:
            return response.content
        else:
            print("Failed to download image:", response)
            return None
    except Exception as e:
        print("Error downloading image:", e)
        return None


def save_thumbnail(img, img_url, folder):
    # Saves the downloaded image to a local folder.
    os.makedirs(folder, exist_ok=True)
    file_name = os.path.join(folder, os.path.basename(img_url.split("?")[0]))
    with open(file_name, "wb") as f:
        f.write(img)
    print("Image saved:", file_name)


def retrieve_thumbnail(conn, post_url, folder="thumbnails"):
    # Downloads and saves the thumbnail of an Instagram post.
    info = conn.info()
    print(f"Fetching {post_url} with proxy {info['proxy']} and user-agent {info['user-agent']}")

    response = conn.get(post_url)
    if not response or response.status_code != 200:
        print("Error fetching page:", response.status_code if response else "No response")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    img_url = retrieve_image_url(soup)
    if not img_url:
        return

    img = download_image(conn, img_url)
    if img is None:
        return

    save_thumbnail(img, img_url, folder)
