from urllib import request, parse

def get(url, *, data={}):
  method= 'GET'
  if data:
    req = request.Request('{}?{}'.format(url, parse.urlencode(data)), method=method)
  else:
    req = request.Request(url, method=method)

  with request.urlopen(req) as res:
    return res.read()

def post(url, *, data='', headers={}, method='post'):
  req = request.Request(url, data, headers, method=method)
  with request.urlopen(req) as res:
    return res.read()
