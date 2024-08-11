import requests
import re
from collections import deque
from bs4 import BeautifulSoup


start = input("What's the starting point: ")
target = input("What's the target: ")

#ai introduced me to beautifulsoup and how to use it shout chatgpt ong
def get_links(link):
    links = set()
    url = f'https://en.wikipedia.org/wiki/{link}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/wiki/') and not re.search(r':', href) and href != '/wiki/Main_Page':
            links.add(href)
    
    return links

def wiki_speedrun(start, target):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_page, path = queue.popleft()

        if current_page == target:
            return path
        
        if current_page in visited:
            continue

        if current_page == "/wiki/Case_sensitivity":
            continue 
        #dude what the hell, its immune to the visited set and this???
        
        visited.add(current_page)

        links = get_links(current_page)

        for link in links:
            queue.append((link, path + [link]))
            print(f"Added", link, "to queue!")
    return("got nothing boss")
path = wiki_speedrun(start, target)
print(path)


