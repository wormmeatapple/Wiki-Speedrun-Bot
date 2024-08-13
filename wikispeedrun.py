import requests
import re
from collections import deque
from bs4 import BeautifulSoup
import time 


def get_links(link):
    links = set()
    url = f'https://en.wikipedia.org{link}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/wiki/') and not re.search(r':', href) and href != '/wiki/Main_Page':
            if href == "/wiki/Case_sensitivity":
                continue
            links.add(href)
    
    return links

def wiki_speedrun(start, target):
    scanned = 0
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_page, path = queue.popleft()

        if current_page == target:
            return (f'Scanned this many pages: {scanned}, and found this path: ', path)
        
        if current_page in visited:
            continue
        
        visited.add(current_page)

        links = get_links(current_page)
        scanned += 1

        for link in links:
            queue.append((link, path + [link]))
            print(f"Added", link, "to queue!")
    return("got nothing boss")


start = ("/wiki/Greenham_Lock")
target = ("/wiki/Canal_lock")

start_time = time.time()
path = wiki_speedrun(start, target)
end_time = time.time()
duration = start_time - end_time

#average time to solve 1 link removed = 25.52 sec
print(f"Time taken: {duration:.2f} seconds")
print(path)








