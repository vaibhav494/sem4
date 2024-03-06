def tournament(l):
    dic={5:[], 10:[], 2:[], 19:[], 13:[], 11:[], 18:[], 6:[], 4:[], 17:[]}
    i=0
    new_list=[]
    while (len(l)>1):
        try:
            if l[i]>l[i+1]:
                dic[l[i]].append(l[i+1])
                new_list.append(l[i])
            else:
                dic[l[i+1]].append(l[i])
                new_list.append(l[i+1])
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

    

