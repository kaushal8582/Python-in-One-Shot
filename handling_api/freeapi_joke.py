import requests

def handel_jokeApi():
  url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
  response = requests.get(url)
  joke_data = response.json()
  
  if joke_data["success"] and joke_data["data"]:
    data = joke_data["data"]
    joke = data["content"]
    return joke
  else:
    raise Exception("failed to fetch joke")
    

def main():
  try:
    joke =  handel_jokeApi()
    print(joke)
  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  main()
  

  
  