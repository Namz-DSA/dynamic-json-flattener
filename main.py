from src.utils.flatten import flatten_json

sample = {
    "user": {
        "id": 1,
        "name": "Namratha",
        "details": {
            "age": 25,
            "city": "Pune"
        }
    }
}

result = flatten_json(sample)

print(result)