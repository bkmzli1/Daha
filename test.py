import socket
import json


dataClear = """{ "type":"auth","userName":"root","password":"root" }"""
data = json.loads(dataClear)
print(type(data))
name = data['userName']

print(name)
