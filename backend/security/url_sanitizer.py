from urllib.parse import urlparse

class URLSanitizer:

    BLOCKED_HOSTS = [
        "127.0.0.1",
        "localhost",
        "169.254.169.254"
    ]

    def validate(self, url: str) -> bool:
        parsed = urlparse(url)

        # Only allow http/https
        if parsed.scheme not in ["http", "https"]:
            raise Exception("Invalid URL scheme")

        # Block internal/local addresses
        for blocked in self.BLOCKED_HOSTS:
            if blocked in parsed.netloc:
                raise Exception("Blocked internal URL")

        return True