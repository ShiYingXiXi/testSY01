import requests, json

url = "http://h5.c-lap.cn/oa_api/public/index/oa/login"

body = "{\"name\":\"超级管理员\", \"password\":\"1198a27c0ce9c9556f4cea38f905f5ae\"}"

headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=body.encode("utf-8"))

text = response.text  # 响应结果
text = json.loads(text)  # 字符串转 Json
text = json.dumps(text, indent=8)  # Json pretty
text = text.encode('utf-8').decode('unicode_escape')  # unicode 转中文

print(text)
