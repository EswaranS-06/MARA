import re


class TextCleaner:

    def clean(self, text: str) -> str:

        # 1. Fix missing spaces between lowercase & uppercase
        # text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

        # 2. Remove references like [1], [a], [D 1]
        text = re.sub(r'\[[^\]]*\]', '', text)

        # 3. Remove multiple spaces
        text = re.sub(r'\s+', ' ', text)

        # 4. Fix spacing around punctuation
        text = re.sub(r'\s([.,!?])', r'\1', text)

        # 5. Add space after punctuation if missing
        text = re.sub(r'([.,!?])([A-Za-z])', r'\1 \2', text)

        # 6. Normalize newlines (optional)
        text = re.sub(r'\n+', '\n', text)

        # 7. Remove weird characters (keep basic ASCII)
        text = re.sub(r'[^\x00-\x7F]+', ' ', text)

        return text.strip()