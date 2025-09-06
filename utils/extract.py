from bs4 import BeautifulSoup
def extract_text(html: str, selector: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    node = soup.select_one(selector)
    return node.get_text(strip=True) if node else None
