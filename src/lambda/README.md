README.md
=========

deploy
------

1. get role
  - `aws iam list-roles | less`
    - or `aws iam list-roles | jq '.Roles[] | select(.RoleName | startswith("${role_name}")) | {"RoleName", "Arn"}'`
2. create function and upload
  - `rm lambda.zip && zip -r lambda.zip .`
  - `aws lambda create-function --function-name pystudy --runtime python3.6 --handler main.handler --role ${role_arn} --zip-file fileb://lambda.zip`
    - `--zip-file` need prefix "fileb://"
3. update function
  - `aws lambda update-function-code --function-name pystudy --zip-file fileb://lambda.zip`
4. invoke: `aws lambda invoke --function-name pystudy outfile`
5. delete function: `aws lambda delete-function --function-name pystudy`

* if you use multi profile add command below ` --profile ${your_profile}` or `export AWS_PROFILE=${your_profile}`
