import requests
url ="https://jsonplaceholder.typicode.com/posts"
params = {"user id" :1} 
response = requests.get(url, params=params, timeout = 10 )
print(final_url := response.url)
posts = response.json()
print("posts by user 1:", len(posts))
print("first post:", posts[0]["title"])
