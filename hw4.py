import requests

response = requests.get("https://blog.csdn.net/qq_37616069/article/details/")
print(response.status_code)
