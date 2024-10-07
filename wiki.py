import wikipediaapi
import time

user_agent = "wiki_game_solver (epicsharkbait82@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page):
    links_list = []
    links = page.links

    for title in links.keys():
        links_list.append(title)

    return links_list

def wikipedia_game_solver(start_page, target_page):
    links = fetch_links(start_page)

    for title in links:
        if title == "Rose Parade":
            print("yippie")
        else:
            print("it aint here:(")

start_page = wiki.page("Pasadena High School (California)")
target_page = wiki.page("Rose Parade")
wikipedia_game_solver(start_page, target_page)

print(fetch_links(start_page))