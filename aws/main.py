import boto3

def s3_list():
  # get s3 buckets
  s3 = boto3.resource('s3')
  for bucket in s3.buckets.all():
    print(bucket.name)

def medialive_channels():
  client = boto3.client('medialive')
  resopnse = client.list_channels()
  print(resopnse)

def main():
  s3_list()
  medialive_channels()

if __name__ == '__main__':
  main()