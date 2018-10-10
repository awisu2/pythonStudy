hands up
--------

```bash
sls create -t aws-python3 -p slspy
cd slspy
sls deploy -v
sls invoke -f hello
sls remove
```

### for your setting

```yaml
provider:
  ...
  region: ap-northeast-1
  profile: ${yourprofile}
```