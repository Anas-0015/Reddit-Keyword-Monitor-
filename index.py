from colorama import Fore, Style
import praw

def main():
    reddit = praw.Reddit(client_id="9SimyCl7uQa3OC3W1Mxeaw",
                         client_secret="ax4NNs44-ecGnZdwK80MMhVAETrjfg" 
                         , user_agent=True)
    


     # Print Start Screen with ASCII Art & Color
    print(Fore.CYAN + "="*40)
    print(Fore.GREEN + "   Welcome to Reddit Keyword Monitor   ")
    print(Fore.CYAN + "="*40)
    print(Fore.YELLOW + "       Created by Anas       ")
    print(Fore.CYAN + "="*40)



    subreddit = input(Fore.YELLOW +"Enter the subreddit you want to monitor (e.g., 'python'): ")
    if not subreddit:
        print(Fore.RED + "Subreddit cannot be empty. Please try again.")
        return
    
    keyword = input(Fore.YELLOW +"Enter the keyword you want to monitor: ")
    if not keyword:
        print(Fore.RED + "Keyword cannot be empty. Please try again.")
        return
    print(Fore.CYAN + "="*40)

    matchs = []
    found = False


    for posts in reddit.subreddit(subreddit).search(keyword, sort="new", limit=10):


        if keyword.lower() in posts.title.lower():
            matchs.append((posts.title, posts.url))
            found = True
            # Print the title of the submission
            print("Title:", posts.title)
            # the reddit post url
            print("URL:", posts.url)
            print("=======================================")

    
    if not found:
        print("No new posts found with the keyword:", keyword)
        print("=======================================")
    else:
        with open("mathed.txt","w") as f :
            for title, url in matchs:
                f.write(f"Title: {title}\n")
                f.write(f"URL: {url}\n")
                f.write("=======================================\n")
        print(Fore.GREEN + f"Results have been saved to 'matches.txt'!")
        print(Fore.CYAN + "="*40)
    
    print(Fore.GREEN +"Monitoring completed. Good bye!")
    print(Fore.CYAN + "="*40)

if __name__ == "__main__":
    main()