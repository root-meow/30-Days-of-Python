actors = ("Tom Hardy", "American", "45")
def tuple_convert(actors):
    name, nationality, age = actors
    return {
        "name": name,
        "nationality":nationality,
        "age":age
    }

print(tuple_convert(actors))




