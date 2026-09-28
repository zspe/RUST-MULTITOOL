import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import colorama
from colorama import Fore, init
import webbrowser
import sys
import os


def fasttypewriter(text, delay=0.0003):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

colorama.init()

ascii2 = """

 ██ ███    █    ██     ▄▄██   ▄▄▄█▄███▓       ▄█▄  ▄    ██ ███    ▄▄▄        █▀   █░  ██▓     ▓ ▄▄██   ██ ███  
▓██ ▒ ██▓  ██  ▓▀█▒ ▒ ▀   ▒   ▓  ██▒ ▓▒      ▓ █▀ ▀█   ▓██ ▒ ██▓ ▒▄▀ █▄     ▓██▓█▒█░ ▓██▒     ▓█   ▀  ▓██ ▒ ██▓
▓██ ░▄█ ▒ ▓██  ▒██░ ░ ▓██▄    ▒ ▓██░ ▒░      ▒▓█    ▄  ▓██ ░▄█ ▒ ▒██  ▀█▄   ▒██▒█░█  ▒██░     ▒█ █    ▓██ ░▄█ ▒
▒▄█▀▀█▄   ▓▓█  ░██░   ▒   ▄█▓ ░ ▓▄█▓ ░       ▒▒▒▄ ▄  ▒ ▒▄█▀▀█▄   ░▄█▄▄▄▄██  ░▒█░█ █  ▒█ ░     ▒▓█  ▄  ▒▄█▀▀█▄  
░██▓ ▒██▒ ▒▒███▄▀▓  ▓███▄▄▀▒▒   ▒██▒ ░       ▒ ▒   ▀ ░ ░██▓ ▒██▒  ▓█   ▓██▒ ░░██▒██▓ ░▄█████▒ ░▒████▒ ░██▓ ▒██▒
░ ▒▓ ░▒▓░ ░▒▓▒ ▒ ▒  ▒ ▒▓▒ ▒ ░   ▒ ░░         ░ ░▒ ▓  ░ ░ ▒▓ ░▒▓░  ▒▒   ▓▒█░  ░ ▓░▒ ▒ ░ ▒░▓  ░ ░░ ▒░ ░ ░ ▒▓ ░▒▓░
  ░▒ ░ ▒░ ░░▒░ ░ ░  ░ ░▒  ░ ░     ░            ░  ▒      ░▒ ░ ▒░   ▒   ▒▒ ░    ▒ ░ ░ ░ ░ ▒  ░  ░ ░  ░   ░▒ ░ ▒░
  ░░   ░   ░░░ ░ ░  ░  ░  ░     ░            ░           ░░   ░    ░   ▒       ░   ░   ░ ░       ░      ░░   ░ 
   ░         ░            ░                  ░ ░          ░            ░  ░      ░       ░  ░    ░  ░    ░     
                                             ░                                                                 
                                                                        | made by zed |
|--------------------------------------------------------------------------------------------------------------------|                                                  
                                                                                                            """                                                                                                                         



def fasttypewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0001)
    print()

ascii = """
             ______________________________________________________
  |          |                                                    /      
  |          | [1.] Crawl Websites       [2.] Scrape Websites.   / 
  |          |    ---------------------  ---------------------  /
  |          | [4.] Help/info            [5.] Github/Discord   /
  |          |  -----------------------  ------------------   /
  |          |    ===================================        /           
  |          |       https://discord.gg/H6Q52BR8H           /
             |_____________________________________________/  
          
  __________________________________________________________________
                                                                """

fasttypewriter(Fore.GREEN + ascii2)
print(ascii)



#actual code down here
#===========================
#  |
#  |
# \ /
#  -


selection = input("\n    |||||   [ [1-3] ]  |> ")

if selection == "1":
    print("\n===================================")
    website = input("URL: |> ")

    if not website.startswith(("http://", "https://")):
        website = "http://" + website

    print("\nTesting to see if website is up...")
     
    try:
        res = requests.get(website, timeout=10)
    except requests.RequestException as q:
        print(f"\nCould not connect to website: {q}")
        input("Enter to close... ")
        sys.exit()

    if res.status_code == 200:
        print("Website is up, proceeding.")

        max_pages_input = input("\nMax Pages to crawl? |> ")
        try:
            max_pages = int(max_pages_input)
            
        except ValueError:
            print("\nInvalid number, defaulting to 10.")
            max_pages = 10

        def crawl(start_url, max_pages):
            visited = set()
            queue = [start_url]
            domain = urlparse(start_url).netloc

            headers = {
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4"
            }

            while queue and len(visited) < max_pages:
                url = queue.pop(0)
                if url in visited:
                    continue

                try:
                    r = requests.get(url, timeout=5, headers=headers)
                    r.raise_for_status()
                except requests.RequestException:
                    print(f"\nFailed {url},")
                    print("\nLikely a file or media type this crawler cannot look at or open.")
                    print("----------------------------------")
                    visited.add(url) #make sure it doesnt crawl the same url multiple time
                    continue

                if r.status_code == 450:
                    print("\nUser Agent Flagged!")
                    print("Try with new Agent?")

                    agentselec = input("\n[y/n] |> ")

                    if agentselec == "y":
                        o = """  
                                 Agent 1: Google Chrome (Win)        Agent 2: Google Chrome (Mac)
                                 ----------------------------        -----------------------------
                                 Agent 3: iPad (Safari)             Agent 4: Googlebot (Search Crawler)                                               
                                -------------------------           -----------------------------------
                                                 Agent 5: Android Phone (Chrome)
                                                                                """

                        print(o)

                        header2 = input("\n[1-5]: ")
                        if header2 == "1":
                            headas = {
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                            }

                            r1 = requests.get(url, timeout=5, headers=headas)

                            if r1.status_code == 200:
                                print("User Agent Rotation worked, continuing.")
                                start()

                        elif header2 == "2":
                            headas = {
                                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                            }

                            r1 = requests.get(url, timeout=5, headers=headas)

                            if r1.status_code == 200:
                                print("User Agent Rotation worked, continuing.")
                                start()

                        elif header2 == "3":
                            headas = {
                                "User-Agent": "Mozilla/5.0 (iPad; CPU OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
                            }

                            r1 = requests.get(url, timeout=5, headers=headas)

                            if r1.status_code == 200:
                                print("User Agent Rotation worked, continuing.")
                                start()

                        elif header2 == "4":
                            headas = {
                                "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
                            }

                            r1 = requests.get(url, timeout=5, headers=headas)

                            if r1.status_code == 200:
                                print("User Agent Rotation worked, continuing.")
                                start()

                        elif header2 == "5":
                            headas = {
                                "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
                            }

                            r1 = requests.get(url, timeout=5, headers=headas)

                            if r1.status_code == 200:
                                print("User Agent Rotation worked, continuing.")
                                start()

                visited.add(url)
                print(f"\nFound {url}")
                print("----------------------------------")

                soup = BeautifulSoup(r.text, "html.parser")
                for link in soup.find_all("a", href=True):
                    new_url = urljoin(url, link["href"]).split("#")[0]
                    parsed = urlparse(new_url)
                    if parsed.scheme in ("http", "https") and parsed.netloc == domain \
                            and new_url not in visited and new_url not in queue:
                        queue.append(new_url)

        def start():
            print("\nCrawling...")
            time.sleep(0.5)
            crawl(website, max_pages)
            print("\n------------------------------------------------------")
            print(f"Finished Crawling {website}")
            input("Enter to close...")

        if __name__ == "__main__":
            start()

    elif res.status_code == 400:
        print("\nWebsite is not up, or responding.")
        print("\nTool cannot proceed.")
        input("Enter to close... ")
    else:
        print(f"\nWebsite returned status code: {res.status_code}")
        print("\nTool cannot proceed.")
        input("Enter to close... ")
#scraper 
elif selection == "2":
    site = input("\nURL?: |> ")

    if not site.startswith(("http://", "https://")):
        site = "http://" + site

    header3 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.22 Safari/537.36"
    }

    try:
        response = requests.get(site, timeout=5, headers=header3)

        if response.status_code == 200:
            print("\nWebsite is up and responding.")
            print("-------------------------------------------------")

            soup = BeautifulSoup(response.text, "html.parser")

            title = soup.title

            if title:
                print(f"\nTitle: {title.get_text(strip=True)}")

            meta_description = soup.find("meta", attrs={"name": "description"})

            if meta_description:
                print(f"Description: {meta_description.get('content', '')}")

            print(f"\nLinks: {len(soup.find_all('a'))}")
            print(f"Images: {len(soup.find_all('img'))}")
            print(f"Forms: {len(soup.find_all('form'))}")
            print(f"Inputs: {len(soup.find_all('input'))}")
            print(f"Buttons: {len(soup.find_all('button'))}")
            print(f"Scripts: {len(soup.find_all('script'))}")
            print(f"Stylesheets: {len(soup.find_all('link', rel='stylesheet'))}")
            print(f"Headings: {len(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']))}")
            print(f"Paragraphs: {len(soup.find_all('p'))}")

            print("\nHeadings")
            print("-------------------------------------------------")

            for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
                text = heading.get_text(" ", strip=True)

                if text:
                    print(f"{heading.name}: {text}")

            print("\nLinks")
            print("-------------------------------------------------")

            for link in soup.find_all("a", href=True):
                text = link.get_text(" ", strip=True)
                href = link.get("href")

                if text:
                    print(f"{text} -> {href}")
                else:
                    print(href)

            print("\nImages")
            print("-------------------------------------------------")

            for image in soup.find_all("img"):
                src = image.get("src")
                alt = image.get("alt")

                if src:
                    print(f"{src} | {alt}")

            print("\nForms")
            print("-------------------------------------------------")

            for form in soup.find_all("form"):
                action = form.get("action")
                method = form.get("method", "GET").upper()

                print(f"Action: {action}")
                print(f"Method: {method}")

                for field in form.find_all(["input", "textarea", "select", "button"]):
                    field_type = field.get("type", field.name)
                    name = field.get("name")
                    field_id = field.get("id")

                    print(f"  {field_type} | name={name} | id={field_id}")

                print()

            print("\nScripts")
            print("-------------------------------------------------")

            for script in soup.find_all("script"):
                src = script.get("src")

                if src:
                    print(src)
                else:
                    script_text = script.get_text(strip=True)

                    if script_text:
                        print("Inline script found")

            print("\nPage Structure")
            print("-------------------------------------------------")

            for element in soup.find_all(["header", "nav", "main", "section", "article", "aside", "footer"]):
                print(element.name)

        elif response.status_code == 400:
            print("\nWebsite is not up or responding to scraper.")
            print("-----------------------------------")

        else:
            print(f"\nFailed to retrieve the webpage. Status code: {response.status_code}")

    except requests.exceptions.Timeout:
        print("\nRequest timed out.")

    except requests.exceptions.RequestException as error:
        print(f"\nRequest failed: {error}")

    input("\nEnter to return to close... ")


elif selection == "4":
    fasttypewriter("\nRUST CRAWLER is a website crawling and scanner tool.")
    fasttypewriter("\nIt crawls and scans for inputs and different information.")
    fasttypewriter("\nGood for gathering info quickly during Bug Bountys or During authorized labs.")
    fasttypewriter("--------------------------------------------------")
    input("\nEnter To Close.. ")

elif selection == "5":
    webbrowser.open("https://github.com/zspe")
    webbrowser.open("https://github.com/zedwed11")
    webbrowser.open("https://github.com/zedwed11/Aya-Multitool")
    webbrowser.open("https://discord.gg/FB7d4HwM4Y")
    print("--------------------------------------------")
    input("\nEnter To Close... ")
    sys.exit()

else:
    print("\nInvalid Option.")
    input("\nEnter to close... ")
    sys.exit()