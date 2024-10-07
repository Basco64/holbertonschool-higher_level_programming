#!/usr/bin/python3

import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"
req = requests.get(url)


def fetch_and_print_posts():
    print(f"Status Code: {req.status_code}")

    if req.status_code == 200:
        posts = req.json()

        for post in posts:
            print(f"{post['title']}")
    else:
        print("Error print")


def fetch_and_save_posts():
    if req.status_code == 200:
        data = []

        posts = req.json()
        for post in posts:
            obj = {
                    "id": post['id'],
                    "title": post['title'],
                    "body": post['body']
                    }
            data.append(obj)

        csv_col = ['id', 'title', 'body']

        with open('posts.csv', mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=csv_col)
            writer.writeheader()
            writer.writerows(data)

    else:
        print("Error save")
