def encoder(myStr):
    prev = myStr[0]
    count = 1
    newStr = ""

    for i in range(1, len(myStr)):
        if prev == myStr[i]:
            count += 1
            prev = myStr[i]
        else:
            newStr += str(count) + prev
            prev = myStr[i]
            count = 1
        if i + 1 >= len(myStr):
            newStr += str(count) + prev
    if len(newStr) > len(myStr):
        return newStr
    else:
        return myStr