import json

with open("my_json.json") as f:
    my_json = json.load(f)

print(my_json)

print(json.dumps(my_json))
print()
print(json.dumps(my_json, ensure_ascii=False))
print()
print(json.dumps(my_json, indent=4))


print(json.dumps("""hello"""))
print(json.dumps(12))
print(json.dumps(1.2))
print(json.dumps(True))
print(json.dumps([True, 1.2, 2, "spam"]))
print(json.dumps((True, 1.2, 2, "spam")))
print(json.dumps({True: 1.2, 2: "spam"}))
print(json.dumps(None))
