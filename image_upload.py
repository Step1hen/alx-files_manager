import base64
import requests
import sys

file_path = sys.argv[1]
file_name = file_path.split('/')[-1]

encoded_file = None
with open(file_path, "rb") as image_file:
    encoded_file = base64.b64encode(image_file.read()).decode('utf-8')

res_json = {'name': file_name, 'type': 'image', 'isPublic': True,
            'data': encoded_file, 'parentId': sys.argv[3]}
res_headers = {'X-Token': sys.argv[2]}

r = requests.post("http://0.0.0.0:5000/files", json=res_json,
                  headers=res_headers)
print(r.json())
