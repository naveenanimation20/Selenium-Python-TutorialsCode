import requests
import json
import jsonpath

# URL = 'https://reqres.in/api/users?page=2'
#
# '''get call'''
# response = requests.get(URL)
# print(response.url)
# print(response.status_code)
# print(response.content)
# print(response.headers['content-type'])
# # print(response.cookies)
# # print(response.encoding)
# # print(response.history)
# # print(response.elapsed)
# json_format = json.loads(response.text)
# print(json_format)
# first_name = jsonpath.jsonpath(json_format, 'data[0].first_name')
# print(first_name)
# assert first_name[0]== 'Michael'
# page = jsonpath.jsonpath(json_format, 'page')
# assert page[0] == 2


'''post call'''
URL = 'https://reqres.in/api/users'
file = open('/Users/NaveenKhunteta/PycharmProjects/Selenium-Demo/API/users.json', 'r')
json_data = file.read()
json_input = json.loads(json_data)
response = requests.post(URL, json_input)
print('status code: ', response.status_code)
print('response body', json.loads(response.text))
