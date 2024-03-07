import requests

def fetch_random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        random_jokes = user_data["content"]
        return random_jokes
    else:
        raise Exception("fetch the user data")
    

def main():
    try:
        random_jokes = fetch_random_jokes()
        print(f"{content}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()