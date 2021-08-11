def comb(x[l],l):
    for i in range(l):
        print('\n')
        print(combo[i],end=" ")
        for j in range(l):
            if(combo[j]!=combo[i]):
                print(combo[j], end=" ")
    combos(x[l],l)
