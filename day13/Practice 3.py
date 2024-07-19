def actor_info_to_dict(actor_tuple):
    name, nationality, age = actor_tuple
    return {
        'name': name,
        'nationality': nationality,
        'age': age
    }
actor_tuple = ("Tom Hardy", "English", 42)
print(actor_info_to_dict(actor_tuple))
