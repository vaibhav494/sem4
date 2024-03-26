def tournament(l):
    dic={5:[], 10:[], 2:[], 19:[], 13:[], 11:[], 18:[], 6:[], 4:[], 17:[]}
    i=0
    new_list=[]
    while (len(l)>1):
        try:
            if l[i] > l[i + 1]:
                winner = l[i]
                loser = l[i + 1]
            else:
                winner = l[i + 1]
                loser = l[i]
            if winner not in dic:
                dic[winner] = []
            dic[winner].append(loser)
            new_list.append(winner)
        except IndexError:
            new_list.append(l[i])
        i+=2
        # print(new_list)
        # print(dic)
        if i>=len(l):
            # print(new_list)
            l=new_list.copy()
            i=0
            new_list=[]
    return max(dic[l[0]])
arr = [5, 10, 2, 19, 13, 11, 18, 6, 4, 17]
print(tournament(arr))

    

