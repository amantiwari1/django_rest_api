import requests
data = {"title":"tiwri","author":"amantiwri3233","email":"amantiwri2333@gmail.com"}

post = requests.post('http://127.0.0.1:8000/articles/', json=data)
print(post.status_code)
