# FoodLionNumBot - FLNB (WIP)
This is a small project I am working on in Python, so it might not be the most beautiful or effective code (as I'm writing this, it's not even finished). I'm also very new to coding, so I apologize for possibly incorrect terminology. I want to post this project in this repository so that I can track how I've modified my code before I get too close to being done. Forgive me if I take a while to upload all the files, I'm very new to GitHub and programming in general.

## Background
I was thinking of random Reddit bot ideas that I could try and program, and I came up with this idea while I was working. I am an employee at Food Lion, a popular grocery store (AFAIK) in the southwest United States. We use a basic PLU system, which seems to be pretty standard. I wanted to incorporate the dozens of PLUs and make it do something. I figured this is a pretty basic thing that I can try and work on.

## Function
FLNB browses through a subreddit's comments and searches for a 4- or 5- digit number. If that number matches a number in the dictionary, it automatically replies with the name of the produce that belongs to that number. For example, if a comment says "I wish I had 4011 cats", then it replies with a new comment that simply says, "Bananas", because 4011 is the PLU for bananas.

## Detailed Explanation
FLNB heavily relies on PRAW, Python Reddit API Wrapper, to communicate with Reddit and send information. The main function opens and asks for an input, and right now the only options are to run the bot and exit the program (see "To Do"). When it runs, it logs the bot into Reddit using config.py. It looks for the document posts_replied_to.txt for the list of comment IDs that have already been replied to, to prevent duplicate responses. It gets the subreddit and number of requests to make with the Reddit server from the code itself (see "To Do").
*The rest is just an idea of how I want to approach the rest of the project, as it is still a WIP.*
The database of PLUs and their associated products are opened if the comment has not already been replied to and contains a number that is 4- or 5- digits long. 
*Thats all I feel like typing tonight- will update more tomorrow*

## To Do
1. Make it work
* Handle underscores being in the fruit name in the dictionary
* Handle if multiple PLU numbers are in a Reddit comment

* "Add" function selector
* "Search" function selector
* "Delete" function selector
* Ability to select subreddit and number of requests before actually running the bot
