import urllib.request, json

HOOK_URL = ''

def post(url, data='', headers=[], method='GET'):
  """
  simple url call
  """
  request = urllib.request.Request(url, data=data, headers=headers, method=method)
  with urllib.request.urlopen(request) as response:
    text = response.read().decode("utf-8")
    return text

def slackPost(text):
  """
  slack post
  """
  data = json.dumps({
    'text': text
  }).encode('utf-8')
  headers = {"Content-Type" : "application/json"}
  return post(HOOK_URL, data, headers, 'POST')

def main():
  try:
    if not HOOK_URL:
      print('please set HOOK_URL')
      return

    res = slackPost('hello3')
    print(res)
  except Exception as e:
    print(e)

if __name__ == "__main__":
  main()
