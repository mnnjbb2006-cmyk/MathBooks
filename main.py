import requests, csv

def get_books(limit=50):
    url = "https://openlibrary.org/search.json"
    headers = {"User-agent":"Mathbooks (mnnjbb.2006@gmail.com)"}
    params = {"q":"", "limit":limit, "subject":"math", "fields":["title", "author_name", "first_publish_year", "publisher"]}
    try:
        res = requests.get(url, headers=headers, params=params)
        return res.json().get("docs",[])
    except Exception as e:
        print(f"Error: {e}")
        exit()

books = get_books(50)

with open("books.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Author", "Year", "Publisher"])
    for book in books:
        writer.writerow([book.get("title", ""), book.get("author_name", [""])[0], book.get("first_publish_year", ""), book.get("publisher", [""])[0]])