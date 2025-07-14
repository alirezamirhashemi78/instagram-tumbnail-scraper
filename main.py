from connection import Connection
from scraper import retrieve_thumbnail
from concurrent.futures import ThreadPoolExecutor
from config import PROXIES, USER_AGENTS  # Use config.py if you want


def run_thumbnail_threads(url_list, proxies, user_agents, max_threads=5):
    conn = Connection(proxies, user_agents)

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(retrieve_thumbnail, conn, url) for url in url_list]
        for f in futures:
            f.result()


if __name__ == "__main__":
    urls = [
        "https://www.instagram.com/p/CNQai0SnJSR/",
        "https://www.instagram.com/p/CPlFsl4KpCA/",
        "https://www.instagram.com/p/CGpm7iUA35B/",
        "https://www.instagram.com/p/CCzwBC_nBTb/",
    ]

    proxies = PROXIES

    user_agents = USER_AGENTS

    run_thumbnail_threads(urls, proxies, user_agents)