def rem(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
            return n 

    # for item in l:
    #     l.remove(word)
    #     return l

l = ["harry", "rohan","shuban","an"]


print(rem(l,"an"))