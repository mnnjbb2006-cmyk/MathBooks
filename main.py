import requests

def get_books(limit=50):
    url = "https://openlibrary.org/search.json"
    headers = {"User-agent":"Mathbooks (mnnjbb.2006@gmail.com)"}
    params = {"q":"math", "limit":limit}
    try:
        res = requests.get(url, headers=headers, params=params)
        return res.json().get("docs",[])
    except Exception as e:
        printf(f"Error: {e}")
        exit()

print(get_books())