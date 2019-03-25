def sortOut(collection):
    count = len(collection)
    i = 1
    while i < count:
        if(collection[i] >= collection[i - 1]):
            i += 1
        else:
            collection.insert(i - 1, collection.pop(i))
            i -= 1
            if(i <= 0):
                i += 1
    return collection

