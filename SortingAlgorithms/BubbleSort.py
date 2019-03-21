def sortOut(collection):
    idxs = frozenset(range(len(collection)))
    for value in collection:
        for idx in idxs:
            if idx > 0:
                if collection[idx - 1] > collection[idx]:
                    collection.insert(idx, collection.pop(idx - 1))
    return collection

