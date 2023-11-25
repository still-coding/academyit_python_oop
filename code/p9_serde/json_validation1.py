from jsonschema import ValidationError, validate
import json 

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {
            "type": "integer",
            "minimum": 18,
        },
        "city": {"type": "string"}
    },
    "required": ["name", "age", "city"]
}

json_str = '{"name": "John", "age": 18, "city": "New York"}'

data = None
try:
    data = json.loads(json_str)
except json.decoder.JSONDecodeError as e:
    print("JSON deserialization failed:", e)
else:
    print("JSON successfully deserialized")

if data:
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        print("JSON validation failed:", e)
    else:
        print("JSON is valid")
