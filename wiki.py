from queue import Queue
import wikipediaapi
import time

#setup stuff
user_agent = "wiki_game_solver (epicsharkbait82@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

#returns list of links
def fetch_links(page):
    links_list = []
    links = page.links

    for title in links.keys():
        links_list.append(title)

    return links_list

def wikipedia_game_solver(start_page, target_page):
    print("working on it...")
    start_time = time.time()

    queue = Queue()
    visited = set()
    parent = {}

    #adds start page to queue and visited
    queue.put(start_page.title)
    visited.add(start_page.title)

    #loops when its not empty
    while not queue.empty():
        #gets next in queue
        current_page_title = queue.get()
        #breaks when we find it
        if current_page_title == target_page.title:
            break

        #fetch all links at current page
        current_page = wiki.page(current_page_title)
        links = fetch_links(current_page)

        #goes through links and adds to queue
        for link in links:
            #is page hasnt been visited
            if link not in visited:
                queue.put(link)
                visited.add(link)
                parent[link] = current_page_title

    #reconsturcting path
    path = []
    page_title = target_page.title
    while page_title != start_page.title:
        path.append(page_title)
        page_title = parent[page_title]

    
    path.append(start_page.title)   
    path.reverse()

    end_time = time.time()
    print("this algorithm took", end_time - start_time, "seconds")
    return path

#start and end pages
start_page = wiki.page("Pasadena High School (California)")
target_page = wiki.page("World War II")
path = wikipedia_game_solver(start_page, target_page)
print(path)