import requests
import re


def get_links(link):
    links = []
    linkpattern = r'(/wiki/[^ "]+)'
    cleanpattern = r'/wiki/()'
    url = f'https://en.wikipedia.org/wiki/{link}'
    response = requests.get(url)
    text = response.text
    dirtylinks = re.findall(linkpattern, text)
    while "/wiki/Main_Page" in dirtylinks:
            dirtylinks.remove("/wiki/Main_Page")
    for l in dirtylinks:
        if ":" not in l:
            links.append(l)
            
    return links

for match in get_links('Orthogonal_defect_classification'):
    print(match)


