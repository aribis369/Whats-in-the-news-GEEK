from urllib.request import urlopen
from urllib.error import HTTPError
import json
from logo import printlogo
from colorama import Fore, Style, Back

cmds = {"international": ["BBC News", "CNN", "Daily Mail", "The Guardian UK", "The New York Times", "The Telegraph"],
        "national": ["The Times of India", "The Hindu"],
        "technology": ["Engadget", "Hacker News", "Techcrunch", "TechRadar", "The Next Web"],
        "sports": ["BBC Sport", "ESPN", "ESPN Cric info", "Fox Sports", "TalkSport"],
        "finance": ["Bloomberg", "Business Insider", "Financial Times", "The Wall Street Journal", "Time", "Fortune"],
        "entertainment": ["BuzzFeed", "Entertainment Weekly", "MTV News", "MTV News UK"],
        "science": ["New Scientist"],
        "blog": ["Reddit r all"],
        "adventure": ["National Geographic"],
        "help": ["help", "exit","list-news","sources"],
        "list-news": ["international", "national", "technology", "sports", "finance", "entertainment", "science", "blog", "adventure"]
        }

# global api key to be given by the user.
api_key = None

def news(source):
    print(" 1. Top News\n 2. Latest News\n 3. Most Popular News\n 4. Return")
    loop = 1
    while loop:
        flag = int(input("[1/2/3/4] >>> "))
        if flag == 1:
            url = "https://newsapi.org/v1/articles?source=" + source + "&sortBy=top&apiKey=" + api_key
            loop = 0
        elif flag == 2:
            url = "https://newsapi.org/v1/articles?source=" + source + "&sortBy=latest&apiKey=" + api_key
            loop = 0
        elif flag == 3:
            url = "https://newsapi.org/v1/articles?source=" + source + "&sortBy=popular&apiKey=" + api_key
            loop = 0
        elif flag == 4:
            loop = 0
            return console()
        else:
            print("Enter a valid number!")

    # using with .. as to allow closing the url connection by python.
    try:
        with urlopen(url) as httpob:
            decob = httpob.read().decode("utf-8")
            jsonob = json.loads(decob)
            news = jsonob["articles"]

    # if api key is Invalid an HTTPError will be thrown.
    except HTTPError as e:
        print("Invalid API")
        create_api_file(file_name)
        return console()

    # draws a border to seperate posts.
    draw_border()
    for n in news:
        print(Fore.RESET)
        try:
            print(Back.YELLOW + src2(jsonob["source"]) + Back.RESET)
            print((Style.BRIGHT +"By: " + n["author"]) + Style.RESET_ALL)
            #Sometimes the author is not provided. For those cases, 'Except' has been put. 
            #If no author provided, The author will be give out to be the news publishing company.
        except:
        	print((Style.BRIGHT +"By: " + src2(jsonob["source"])) + Style.RESET_ALL)
        try:
            print(Back.RED + (Style.BRIGHT + n["title"] + Style.RESET_ALL)) 
            print(Fore.BLUE + n["description"] + Fore.RESET)
        except:
            print(Fore.RED + "SOME ERROR OCCURED!!!\n" + Fore.RESET)
        print(Back.BLUE +(Style.BRIGHT + "url: "+ n["url"]) + Style.RESET_ALL + Back.RESET)
        #Similar to author, sometimes the Publishing time is not provided. 
        #For those cases, there will be no publishing time put. So except case has been made.
        try:
        	print(Fore.GREEN + "Published At: "+ n["publishedAt"] + Fore.RESET )
        except:
        	draw_border()
        	continue
        draw_border()

def sour(): 
	#The is just one url for sources function and no further modification to it required,
	#Hence url has been initialised at the starting for the same.
    url = "https://newsapi.org/v1/sources?language=en"
    try:
        with urlopen(url) as httpob:
            decob = httpob.read().decode("utf-8")
            jsonob = json.loads(decob)
            sources = jsonob["sources"]

    except HTTPError as e:
        print("Invalid API")
        create_api_file(file_name)
        return console()

    draw_border()
    key = 1
    for s in sources:
        print(Fore.RESET)
        try:
            print(key, end="")
            print(". " + Back.BLUE + (Style.BRIGHT +s["name"] + Style.RESET_ALL) + Back.RESET)
            key = key+1
        except:
            print(Fore.RED + "SOME ERROR OCCURED!!!\n" + Fore.RESET)
    draw_border()
    #Incase more detailed description of the source required.
    print("Enter the index of any source if you want to know more about it.\nEnter -1 for returning back to main menu\n")
    loop = True
    while loop:
        flag = input(">")
        try:
            if flag == '-1':
                loop = False
            elif int(flag)>0 or int(flag)<60:
                s = sources[int(flag) -1]
                print('\n')
                print(Back.BLUE + (Style.BRIGHT +s["name"] + Style.RESET_ALL) + Back.RESET)
                print("Description: " + Fore.BLUE + s["description"] + Fore.RESET)
                print("Category: " + Fore.RED + s["category"] + Fore.RESET)
                print("Url: " + Fore.GREEN + (Style.BRIGHT + s["url"]) + Fore.RESET)
                print("\nEnter any other index. Enter -1 to exit\n")            
        except:
            print("Invalid Entry!\n")

def draw_border():
    width = 80
    print(Style.BRIGHT+"-" * width +Style.RESET_ALL+"\n")

def src(n):
    k = n.replace(" ", "-")
    return k

def src2(n):
	k = n.replace("-"," ")
	return k

def create_api_file(file_name):
    """
    This method creates a new file, with the name
    'file_name'.

    This file will store the api key for the user.
    """
    global api_key
    api_key = input("Enter a valid API key: ")

    with open(file_name, "w") as f:
        f.write(api_key + '\n')
    f.close()
    print("The API key is: " + api_key)

def get_api():
    global api_key 

    # the api once entered will be stored in this file.
    global file_name 
    file_name = "user-api.txt"

    try:
        f = open(file_name, "r") 
        api_key = f.readline()
        f.close()
        print("The API key is: " + api_key)
        print("Do you want to change the API key? [Y/N]\n")
        flag = input()
        if flag == 'Y':
            create_api_file(file_name)


    # if the file was not found then create the file and store the api.
    except FileNotFoundError:
        create_api_file(file_name)

    # if the api_key in the file was not present (i.e, empty file)
    # get the api from the user.
    if api_key == None or len(api_key) == 0:
        create_api_file(file_name)

def console():
    while True:
        cmd = input(">>> ")

        # command is invalid
        if (cmd not in cmds["list-news"] and cmd not in cmds["help"]):
            print(Fore.RED + "WRONG COMMAND!!!")
            print(Fore.GREEN + "Try these COMMANDS" + Fore.RESET)
            for c in cmds["help"]:
                print("    " + c)

        # help command
        elif cmd == "help":
            print(Fore.GREEN + "Try these COMMANDS" + Fore.RESET)
            for c in cmds["help"]:
                print("    " + c)

        # list command
        elif cmd == "list-news":
            print(Fore.GREEN + "Find news about any of these topics" + Fore.RESET)
            for l in cmds["list-news"]:
                print("    " + l)

        # exit command
        elif cmd == "exit":
            print(Style.RESET_ALL)
            exit()

        elif cmd == "sources":
            sour()

        # show news
        else:
            for n in cmds[cmd]:
                s = src(n)
                news(s)

if __name__ == "__main__":
    printlogo()
    print(Style.DIM + "powered by NewsAPI.org\n" + Style.NORMAL)

    # get the user api first.
    get_api()

    # display the console.
    console()