def fetchItemsToDisplay(numOfItems, items, sortParameter, sortOrder, itemsPerPage, pageNumber):
    order = False
    if sortOrder == 1:
        order = True

    res = []
    currPage = 0
    currItems = 1
    sortKey = [lambda x: x, lambda x: items[x][0], lambda x: items[x][1]]
    for name in sorted(items, reverse=order,
                       key=sortKey[sortParameter]):  # sort: O(nlogn) loop: O(n) -> Total: O(nlogn + n) = O(nlogn)
        # print(name, items[name]) # Uncomment to see the sorting order
        if currPage > pageNumber:
            break
        if currPage == pageNumber:
            res.append(name)
        if currItems == itemsPerPage:
            currItems = 1
            currPage += 1
        currItems += 1

    return res