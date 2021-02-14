#write a function to check if two lists are anagram
#anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
def anagram(s, t):
    alist = list(s)
    blist = list(t)

    alist.sort()
    blist.sort()

    if len(s) != len(t):
        return False

    matches = True
    for i in range(len(s)):
        if alist[i] != blist[i]:
            return False
    return matches