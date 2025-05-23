
# Reddit Keyword Monitor

**Reddit Keyword Monitor** is a Python-based CLI tool that monitors Reddit for new posts containing a specific keyword in the title, within a specified subreddit. The program fetches the latest posts and displays matching results in the terminal. If matches are found, they are saved to a text file for later reference.

## Features:
- **Monitor Subreddits**: Allows you to choose a subreddit to monitor.
- **Search for Keywords**: Search for specific keywords within post titles.
- **Display Results**: View the title and URL of the posts that match your keyword.
- **Save Results**: All matched posts are saved to a text file (`matches.txt`) for later viewing.

## Technologies Used:
- **Python**: The main programming language.
- **PRAW (Python Reddit API Wrapper)**: Interact with Reddit’s API to fetch posts.
- **Colorama**: Adds colored text output for better readability in the terminal.
- **File I/O**: Saves matched results to a text file.

## Installation:

### 1. Clone the repository
Clone the repository to your local machine using the following command:
```bash
git clone https://github.com/Anas-0015/Reddit-Keyword-Monitor.git
```

### 2. Install required libraries
The project requires the following Python libraries: `praw` and `colorama`. You can install them by running:
```bash
pip install praw colorama
```

### 3. Configure Reddit API Credentials
To use the Reddit API, you'll need to create a Reddit application and get the following credentials:
- `client_id`
- `client_secret`
- `user_agent`

Create an application [here](https://www.reddit.com/prefs/apps), then replace these credentials in the script `reddit_keyword_monitor.py` where it says `client_id`, `client_secret`, and `user_agent`.

## How to Run:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the Python script:
```bash
python reddit_keyword_monitor.py
```
4. The program will prompt you to:
   - Enter the subreddit you want to monitor (e.g., `python`, `learnprogramming`).
   - Enter the keyword you want to monitor within the subreddit.
5. The program will search the latest posts and display results on the terminal. If any posts match the keyword, their titles and URLs will be shown. Results will also be saved in `matches.txt`.

## Example Flow:

```
========================================
   Welcome to Reddit Keyword Monitor   
========================================
       Created by Anas       
========================================
Enter the subreddit you want to monitor (e.g., 'python'): python
Enter the keyword you want to monitor: programming
========================================
Title: Learn programming with Python
URL: https://www.reddit.com/r/python/comments/xyz123/learn_programming_with_python/
=======================================
Results have been saved to 'matches.txt'!
========================================
Monitoring completed. Good bye!
========================================
```

## File Structure:
```
Reddit-Keyword-Monitor/
├── reddit_keyword_monitor.py      # The main Python script
└── matches.txt                    # File where results are saved (generated after monitoring)
```

## Contributing:
Feel free to fork this repository, make changes, and submit a pull request! Any suggestions or bug fixes are greatly appreciated.

## License:
This project is open-source and available under the [MIT License](LICENSE).

## Contact:
Created by Anas (You can contact me via GitHub).

## GitHub Repository:
[https://github.com/Anas-0015/Reddit-Keyword-Monitor](https://github.com/Anas-0015/Reddit-Keyword-Monitor)
