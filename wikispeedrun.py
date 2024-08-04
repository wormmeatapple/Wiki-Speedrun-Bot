import requests
import re


def get_links(link):
    pattern = r'(/wiki/[^ "]+)'
    url = f'https://en.wikipedia.org/wiki/{link}'
    response = requests.get(url)
    text = response.text
    links = re.findall(pattern, text)

    return links

for match in get_links('Shed'):
    print(match)


