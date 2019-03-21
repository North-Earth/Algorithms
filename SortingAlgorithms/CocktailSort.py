def sortOut(collection):
    idxs = list(range(len(collection)))
    count = len(idxs)

    while count > 0:
        for idx, value in enumerate(idxs):
            if (idx > idxs[0] and collection[value] < collection[value - 1]):
                collection.insert(value, collection.pop(value - 1))
        idxs.pop()
        idxs.reverse()

        if len(idxs) == 0:
            break

        for idx, value in enumerate(idxs):
            if (idx < idxs[0] and collection[value] < collection[value - 1]):
                collection.insert(value, collection.pop(value - 1))
        idxs.pop()
        idxs.reverse()

        count = len(idxs)
    return collection

