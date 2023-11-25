from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(max_length=32)
    age: int = Field(ge=18)
    city: str


json_str = '{"name": "John", "age": 30, "city": "New York"}'

user = User.model_validate_json(json_str) # валидация
print(user)

print(user.model_dump_json(indent=4)) # сериализация
