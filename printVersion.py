import requests
print('The current requests library version is: ', requests.__version__)

#var = requests.get('http://www.google.com')

var = requests.get("https://raw.githubusercontent.com/PENGYUXIONG/cmput404lab1/master/printVersion.py")
print(var.content)
