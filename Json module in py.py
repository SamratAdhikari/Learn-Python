# Java Script Object Notation

import json

data = '{"var": "samrat", "var1" : 7}'
print(data)

parsed = json.loads(data)
print(parsed["var"])


data1 = {
    "name" : "Samrat",
    "cars" : ["Lamborghini Gallardo", "Rolls Royce", "Mustang GT"],
    "MCQ" : False
}

# make py code compatible for js
jscomp = json.dumps(data1)
print(jscomp)

#task = what is sort_keys parameter in dumps

