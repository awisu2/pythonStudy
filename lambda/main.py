def handler(event, context):
  print(repr(event), repr(context))
  return "hello world"
