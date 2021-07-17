# Python program to convert
# Python to JSON
#json.dumps() method can convert a Python object into a JSON string.
import json

dictionary = {
    "id": "04",
    "name": "sunil",
    "depatment": "HR"
}

# Serializing json
json_obj=json.dumps(dictionary, indent=4)
print(json_obj)