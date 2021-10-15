"""Simple script to obtain an API token via OAuth."""
import webbrowser
from argparse import ArgumentParser
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict
from urllib.parse import urlencode

import requests

HOST_NAME = "localhost"
SERVER_PORT = 8080
REDIRECT_PATH = "/oauth/return"


class OAuthDancer:
    """A class to help with completing the OAuth dance."""

    base_url: str = "https://connect.deezer.com"
    app_id: str
    app_secret: str
    redirect_url: str = f"http://{HOST_NAME}:{SERVER_PORT}{REDIRECT_PATH}"

    def __init__(self, app_id: str, app_secret: str) -> None:
        self.app_id = app_id
        self.app_secret = app_secret

    def get_auth_page(self):
        """Build the URL of the auth page where the process starts."""
        query = urlencode(
            {
                "app_id": self.app_id,
                "redirect_uri": self.redirect_url,
                "perms": ",".join(
                    [
                        "basic_access",
                        "email",
                        "manage_library",
                        "delete_library",
                        "listening_history",
                    ]
                ),
            }
        )
        return f"{self.base_url}/oauth/auth.php?{query}"

    def get_token(self, code: str) -> Dict[str, str]:
        """Make the API call to obtain the token."""
        query = urlencode(
            {
                "app_id": self.app_id,
                "secret": self.app_secret,
                "code": code,
            }
        )
        url = f"{self.base_url}/oauth/access_token.php?{query}"
        response = requests.get(url)
        content = response.content.decode()
        # The body looks like this: 'access_token=blah&expires=1234'
        # -> parse this to a dictionary
        return dict(tuple(p.split("=", 1)) for p in content.split("&"))


class MyServer(BaseHTTPRequestHandler):
    """Simple HTTP request handler to perform the OAuth dance."""

    def do_GET(self) -> None:
        """Route GET requests to the right handler."""
        if self.path.startswith(REDIRECT_PATH):
            self.redirect_route()
        else:
            self._render_content(
                f'<a href="{self.oauth_dancer.get_auth_page()}">Start Oauth Flow</a>'
            )

    def redirect_route(self) -> None:
        """
        Handle the redirect route.

        Once the OAuth is approved, Deezer redirects to this route with `?code=blah`
        at the end of the URL.

        Grab this code, make the API call to obtain the token and display it.
        """
        route, params_str = self.path.split("?", 1)
        query_params = dict(p.split("=", 1) for p in params_str.split("&"))
        token_data = self.oauth_dancer.get_token(query_params["code"])
        self._render_content(
            f"Token = {token_data['access_token']}"
            f"<br>"
            f"Expires = {token_data['expires']}"
        )

        # Write token to .env file
        with open(".env", "w+") as file:
            file.writelines(["API_TOKEN=" + token_data["access_token"] + "\n"])
            print("Token written to .env file")
        raise SystemExit("All Done")

    def _render_content(self, content: str):
        """Render the provided content in a HTML page."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes(
                "<html>"
                "<head><title>Deezer API OAuth dancer</title></head>"
                "<body>"
                f"<p>{content}</p>"
                "</body>"
                "</html>",
                "utf-8",
            )
        )

    @property
    def oauth_dancer(self):
        """Shortcut to access the `OAuthDancer` instance."""
        return self.server.oauth_dancer


if __name__ == "__main__":
    # Parse command line options
    parser = ArgumentParser()
    parser.add_argument("--app-id", type=str, required=True)
    parser.add_argument("--app-secret", type=str, required=True)
    args = parser.parse_args()

    # Start local webserver
    webserver = HTTPServer((HOST_NAME, SERVER_PORT), MyServer)

    # Commence OAuth Dance
    webserver.oauth_dancer = OAuthDancer(app_id=args.app_id, app_secret=args.app_secret)
    start_url = webserver.oauth_dancer.get_auth_page()
    print(f"Opening {start_url} in web browser...")
    webbrowser.open(start_url)

    # Wait for user action and display token when finished
    try:
        webserver.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        webserver.server_close()
