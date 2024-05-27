import http.client

conn = http.client.HTTPSConnection("www.google.com")
conn.request("GET", "/")
response = conn.getresponse()
text = response.read().decode("utf-8")
print(text)
conn.close()

