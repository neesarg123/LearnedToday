import os
import requests
from datetime import datetime


NOTION_API_KEY = os.getenv('NOTION_API_KEY')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

headers = {
    'Authorization': f"Bearer {NOTION_API_KEY}",
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28',
}


def make_db_entry():
    main_text = input("What did you learn today? Express your heart ❤\n")
    topic_h = input("Give your learning a high-level topic (1 word, for example, 'Math')\n")
    topic_m = input("Now get a little specific, give it a medium-level topic (1-2 words, like 'Linear Algebra')\n")
    topic_l = input("Finally, a more specific, low-level topic (1-3 words, like 'Vector Multiplication')\n")

    data = {"parent": {
                "database_id": NOTION_DATABASE_ID
            },
            "properties": {
                "Name": {
                  "title": [
                    {
                      "text": {
                        "content": main_text
                      }
                    }
                  ],
                },
                "Date": {
                      "type": "date",
                      "date": {
                        "start": datetime.today().strftime('%Y-%m-%d')
                      }
                    },
                "Topic-H": {
                  "id": "%3AcrI",
                  "type": "select",
                  "select": {
                    "name": topic_h
                  }
                },
                "Topic-M": {
                  "id": "%3AcrI",
                  "type": "select",
                  "select": {
                    "name": topic_m
                  }
                },
                "Topic-L": {
                  "id": "%3AcrI",
                  "type": "select",
                  "select": {
                    "name": topic_l
                  }
                }
              }
            }

    response = requests.post('https://api.notion.com/v1/pages', headers=headers, json=data)
    if response.status_code == '200':
        print("\nEntry Added!\n")


def main():
    go = True

    while go:
        make_db_entry()

        again = input("Press Enter to create another entry!")
        if again != "":
            go = False


main()
