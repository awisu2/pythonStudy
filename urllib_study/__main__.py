from request import get, post
import json

URL = 'https://www.google.co.jp/'

def main():
  data = {
    'foo': 123,
  }
  body = get(URL, data=data)
  print(body)

  # method not allowed
  data = {
      'foo': 123,
  }
  headers = {
    'Content-Type': 'application/json',
  }
  post(URL, data=json.dumps(data).encode(), headers=headers)

if __name__ == "__main__":
  main()
