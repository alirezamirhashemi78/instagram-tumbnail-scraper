# Instagram Thumbnail Scraper

A Python scraper to download thumbnail images from Instagram posts and reels using multithreading for faster performance.  
The project automatically rotates proxies and user-agents every 10 requests to reduce the risk of being blocked by Instagram.

---

## Features

- Download thumbnails from Instagram posts and reels by URL
- Supports processing multiple URLs concurrently using multithreading (default 5 threads)
- Automatically rotates proxy and user-agent every 10 requests
- Skips proxies if none are provided or if a proxy is invalid
- Modular design with clear separation of concerns

---

## Project Structure

- **config.py**  
  Stores proxy list, user-agent strings, and HTTP headers.  
  If the proxy list is empty or contains invalid proxies, requests will be sent without proxies.

- **connection.py**  
  Contains the `Connection` class to manage HTTP sessions.  
  Handles automatic rotation of proxies and user-agents every 10 requests.

- **scraper.py**  
  Functions to extract thumbnail URLs from Instagram pages, download, and save images locally.

- **main.py**  
  Entry point for the script.  
  Takes a list of Instagram URLs and uses multithreading to download thumbnails concurrently.

---

## Usage

1. **Configure your proxies and user-agents in `config.py`.**  
   Leave the proxy list empty if you do not want to use proxies.

2. **Add Instagram post/reel URLs to the `urls` list in `main.py`.**

3. **Run the script:**  
   python main.py
