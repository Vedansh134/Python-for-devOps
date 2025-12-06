arn = "arn:aws:lambda:us-east-1:123456789012:function:my-lambda-function"

# find aws service name in arn
print(arn.split(":")[-1])