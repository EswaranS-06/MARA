import requests
from bs4 import BeautifulSoup


class URLLoader:
    def __init__(self, url: str):
        self.url = url

    def load(self) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(self.url, headers=headers, timeout=10)

        if response.status_code != 200:
            raise Exception(f"Failed to fetch URL: {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unwanted tags
        for tag in soup(["script", "style", "iframe", "noscript"]):
            tag.decompose()

        # 🔥 Target main Wikipedia content
        content = soup.find("div", class_="mw-content-ltr mw-parser-output")

        if not content:
            raise Exception("Main content not found")

        extracted_text = []

        # Iterate through elements in order
        for element in content.find_all(["p", "div"], recursive=True):

            # ✅ Paragraphs
            if element.name == "p":
                text = element.get_text(separator=" ", strip=True)
                if text:
                    extracted_text.append(text)

            # ✅ Headings (h2, h3 via div class)
            elif element.name == "div":
                classes = element.get("class", [])

                if "mw-heading mw-heading2" in classes or "mw-heading mw-heading3" in classes:
                    heading = element.get_text(strip=True)
                    if heading:
                        extracted_text.append(f"\n\n### {heading}\n")

        return "\n".join(extracted_text)