import re
import requests

localhost = "127.0.0.1:8080"
proxy = {"http": localhost, "https": localhost }

hbin = "http://httpbin.org/absolute-redirect/3"

gerb = "https://cdn.abo.media/upload/article/res/770-430/o_1e1ejt5n4li8hnkd0e1oaa1msh3o.jpg"

hbin = "http://httpbin.org/absolute-redirect/3"
#response = requests.get(gerb, proxies=proxy, stream=True, verify=False )
upload = "http://httpbin.org/anything"

with open ("gerb.jpg", "rb") as f:
    requests.post(upload, proxies=proxy, data=f)

