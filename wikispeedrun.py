import requests
import re
from collections import  deque


start = input("What's the starting point: ")
target = input("What's the target: ")

def get_links(link):
    links = []
    linkpattern = r'(/wiki/[^ "]+)'
    url = f'https://en.wikipedia.org/wiki/{link}'
    response = requests.get(url)
    text = response.text
    dirtylinks = re.findall(linkpattern, text)
    while "/wiki/Main_Page" in dirtylinks:
            dirtylinks.remove("/wiki/Main_Page")
    for l in dirtylinks:
        if ":" not in l and l not in links:
            links.append(l)
            
    return set(links)

def wiki_speedrun(start, target):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_page, path = queue.popleft()

        if current_page == target:
            return path
        
        if current_page in visited:
            continue
        
        visited.add(current_page)

        links = get_links(current_page)

        for link in links:
            queue.append((link, path + [link]))
            print(f"Added", link, "to queue!")

path = wiki_speedrun(start, target)
print(path)








