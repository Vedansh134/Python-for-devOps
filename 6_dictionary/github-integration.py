import requests

# /repos/{owner}/{repo}/pulls     - it is api example
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# response is object of requests library
print(response.status_code)
#print(response.json())

complete_detail = response.json()
print(complete_detail[0]["user"]["login"])

for i in range(len(complete_detail)):
    print(f"{i} : {complete_detail[i]['user']['login']}")



