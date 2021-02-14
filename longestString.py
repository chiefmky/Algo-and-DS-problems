def longest_st(S, slist, longest=''):
    if S in slist and len(S) > len(longest):
        return S
    else:
        for i in range(len(S)):
            longest = longest_st(S[:i] + S[i + 1:], slist, longest)
    return longest

if __name__ == '__main__':
    W = "abppplee"
    D= {"able", "ale", "apple", "bale", "kangaroo"}

    print(longest_st(W,D))
