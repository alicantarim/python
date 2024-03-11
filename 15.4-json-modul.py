# dict

# person = {"name":"Ali","languages":["python","C#"]}

# result = person["name"]
# result = person["languages"]
# result = person["languages"][0]

import json

person_string = '{"name":"Ali","languages":["python","C#"]}'  # JSON string 

person_dict = {
    "name": "Ali",
    "languages": ["Python","C#"]
}

# from JSON string to Dict

# result = json.loads(person_string)  #
# result = result["name"]
# result = result["languages"]


# Dosyadan Json bir bilgiyi okumak

# with open("15.4.0-person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])



# from Dict to JSON string

# result = json.dumps(person_dict)
# print(result)
# print(result["name"]) # Strin olduğu için içindeki her hangi bir alana ulaşamayız.


# Dosyaya Json bilgiyi yazmak

# with open("15.4.0-person.json","w") as f:
#     json.dump(person_dict, f)



person_dict = json.loads(person_string)


result = json.dumps(person_dict, indent= 4, sort_keys= True)
print(person_dict)
print(result)

        # {'name': 'Ali', 'languages': ['python', 'C#']}   --> print(person_dict)

        # {         
        #     "languages": [
        #         "python",
        #         "C#"               --> print(result)   
        #     ],
        #     "name": "Ali"
        # }