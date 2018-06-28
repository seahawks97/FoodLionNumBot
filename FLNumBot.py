# FoodLionNumBot (FLNB) v0.1 by /u/Ndog1000
# Project Started: 12 June 2018
# Python v3.6.3
# Finished v0.1: ?
# This version has easy-to-read comments, and extra prints() for easy reading in shell
#

import praw
import os
import config
import csv


def main():
    print("Welcome to the FoodLionNumBot by /u/Ndog1000!")
    while True:
        selection = input_selection()
        if selection == "q":
            print("Goodbye!")
            exit(1)
        elif selection == "r":          # (R)un bot
            print("Running...")
            r = login_bot()
            posts_replied_to = get_saved_comments()
            run_bot(r, posts_replied_to)

        #elif selection == "a":         # (A)dd an item

        #elif selection == "s":         # (S)earch for an item

        #elif selection == "d":         # (D)elete an item

        else:
            print("Input not recognized. Please enter a valid command.\n")


def input_selection():
    selection = input("What would you like to do? (R)un bot; (Q)uit: ").lower()
    return selection
    # Add, Search, and Delete are not implemented yet


def login_bot():
    print("Logging in...")
    reddit_name = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "Reddit bot: FoodLionNumBot by /u/Ndog1000")
    print("Reddit username: " + str(reddit_name.user.me()))
    print("Logged in!")
    return reddit_name


def get_saved_comments():
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))
    return posts_replied_to


def run_bot(r, posts_replied_to):
    print("Grabbing subreddit...")
    subreddit = r.subreddit("test")  # Put subreddit here
    print("Grabbing comments...")
    comments_list = subreddit.comments(limit=10)  # Put number of requests  here

    with open("FLNB_dict.txt", "r") as db:
        mydict = dict(csv.reader(db))           # Opens the dictionary

    for comment in comments_list:
        if len(comment.body) < 4 or comment in posts_replied_to:
            continue
        else:
            comment_keys = list(int(s) for s in comment.split() if s.isdigit() )        #

        # Finds a comment not replied to, and contains a 4 or 5 digit number
        if comment not in posts_replied_to and comment_keys != []:
            print("Numbers found in comment! Comment ID: " + comment.id)
            for i in comment_keys:
                dict_val = mydict.get(i)
                dict_values = []
                dict_values = dict_values.append(dict_val)
                #comment.reply(dict_values)                                 # Comment out for editing

            # Appends comment ID to post_replied_to.txt
            with open("posts_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")


def txt_to_dict():
    with open("FLNB_dict.txt", "f") as db:
        mydict = dict(csv.reader(db))
    return mydict


main()