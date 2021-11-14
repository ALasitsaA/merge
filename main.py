def merge(*lists):
    prototıp01_list = []
    for anlamadım in lists:
        prototıp01_list += anlamadım
        prototıp01_list.sort()
    return prototıp01_list

print (merge(*lists))
