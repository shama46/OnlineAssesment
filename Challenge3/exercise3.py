d = {"a": 3, 'b': [4, 5, {"c": 56}]}
e = {"a":{"b":{"c":"d"}}}

def value_extractor(dictonary, key):
## we are extracting key and value using k,v by loading  the dictonary using data.items
    for k, v in dictonary.items():
        ## we are matching key with the value 
        if k == key:
            return v
        ## isinstance is a python function which check if the the returned value is dictonary
        elif isinstance(v, dict):
            return value_extractor(v, key)
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    return value_extractor(i, key)

value=value_extractor(d, "b")
print(value)