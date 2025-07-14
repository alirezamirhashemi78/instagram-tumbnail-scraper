import requests
import random


class Connection:
    # Manages HTTP sessions, proxies, and user agents for requests.

    def __init__(self, proxies, user_agents, headers=None):
        # Initialize with lists of proxies, user agents, and optional headers.
        self.proxies = proxies.copy() if proxies else []
        self.user_agents = user_agents
        self.headers = headers or {}
        self.session = None
        self.user_agent = None
        self.rotate_request_count = 0
        self.total_request_count = 0
        self.current_proxy = None
        self._create_new_session()


    def _create_new_session(self):
        # Creates a new session with a rotated user-agent.
        self.session = requests.Session()
        self._rotate_user_agent()
        self.session.headers.update(self.headers)


    def _rotate_user_agent(self):
        # Chooses a new random user-agent and sets it in session headers.
        self.user_agent = random.choice(self.user_agents)
        self.session.headers["User-Agent"] = self.user_agent


    def rotate(self):
        # Rotates proxy and user-agent after every 10 requests.
        self.rotate_request_count += 1
        self.total_request_count += 1

        if self.rotate_request_count >= 10:
            self._create_new_session()
            self.rotate_request_count = 0

        if self.proxies:
            self.current_proxy = random.choice(self.proxies)
        else:
            self.current_proxy = None


    def get(self, url):
        # Sends a GET request using the current session and proxy.
        self.rotate()

        try:
            if self.current_proxy:
                response = self.session.get(
                    url,
                    proxies={"http": self.current_proxy, "https": self.current_proxy},
                    timeout=10,
                )
            else:
                response = self.session.get(url, timeout=10)
            return response
        except Exception as e:
            print("Error during request:", e)
            # If proxy fails, fallback to no proxy
            try:
                response = self.session.get(url, timeout=10)
                return response
            except Exception as e:
                print("Fallback request failed:", e)
                return None


    def info(self):
        # Returns information about the current session: proxy, user-agent, total requests.
        return {
            "proxy": self.current_proxy,
            "user-agent": self.user_agent,
            "total_requests": self.total_request_count,
        }
