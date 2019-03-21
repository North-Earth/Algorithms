def sortOut(collection):
    steeps = frozenset(range(len(collection)))
    for item in collection:
        for steep in steeps:
            if steep > 0:
                if collection[steep - 1] > collection[steep]:
                    collection.insert(steep, collection.pop(steep - 1))
    return collection

