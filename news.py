ffrom urllib.request import urlopen
import json
from logo import printlogo
from colorama import Fore,Style,Back



class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


k=0
cmds={"international":["BBC News","CNN","Daily Mail","The Guardian UK","The New York Times","The Telegraph"],
      "national":["The Times of India","The Hindu"],
      "technology":["Engadget","Hacker News","Techcrunch","TechRadar","The Next Web"],
      "sports":["BBC Sport","ESPN","ESPN Cric info","Fox Sports","TalkSport"],
      "finance":["Bloomberg","Business Insider","Financial Times","The Wall Street Journal","Time","Fortune"],
      "entertainment":["BuzzFeed","Entertainment Weekly","MTV News","MTV News UK"],
      "science":["New Scientist"],
      "blog":["Reddit r all"],
      "adventure":["National Geographic"], 
      "help":["international","national","technology","sports","finance","entertainment","science","blog","adventure","help","exit"],
      "list":[]}

def news(source):
    # get your own api key from newsapi.org and paste in place of this random api key
    # program will not work with the underlying api key
    api_key="b8f5769bc5ce4dae8f362575e4a932f8"
    httpob=urlopen("https://newsapi.org/v1/articles?source="+source+"&sortBy=top&apiKey="+api_key)
    decob=httpob.read().decode("utf-8")
    jsonob=json.loads(decob)
    news=jsonob["articles"]
    print(color.BOLD+"--------------------------------------------------------------------------------"+"\n")
    for n in news:
        print(Fore.RESET)
        try:
            print(Back.YELLOW+jsonob["source"]+Back.RESET)
            print(Back.RED+((color.BOLD+n["title"]+color.END))+color.END)
            print(color.DARKCYAN+n["description"]+color.END)
        except:
            print(Fore.RED+"SOME ERROR OCCURED!!!\n"+Fore.RESET)
            console() 
        print(Fore.YELLOW+"want to read more:"+Back.RESET)
        print(Fore.WHITE+(Style.DIM+n["url"]))
        print(Style.NORMAL)
        print(Fore.MAGENTA+"powered NewsAPI.org")
        print(Style.NORMAL)
        print(color.BOLD+"--------------------------------------------------------------------------------"+"\n")

def logo():
    print("What's in the news?GEEK!!!\n")
    printlogo()
    print(Style.DIM+"powered by NewsAPI.org\n"+Style.NORMAL)

def src(n):
    k=n.lower().replace(" ","-")
    return(k)  

def console():
    global k
    if k==0:
        logo()
        k=1
    
    cmd=input(">>>")
    if cmd not in cmds["help"]:
        print(color.RED+"WRONG COMMAND!!!") 
        print(color.GREEN+"Try these COMMANDS"+color.END)
        for c in cmds["help"]:
            print("    "+c)
        console()
    elif cmd!="help" and cmd!="list"and cmd!="exit":
        for n in cmds[cmd]:
            s=src(n)
            news(s)
        console()
    elif cmd=="help":
        print(color.GREEN+"Try these COMMANDS"+color.END)
        for c in cmds["help"]:
            print("    "+c)
        console()
    elif cmd=="list":
        for l in cmds["list"]:
            print(l+"\n")
    else:
        exit()


if __name__=="__main__":
    console()
