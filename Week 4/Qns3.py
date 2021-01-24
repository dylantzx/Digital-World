def find_average(ls_ls):
    a=0 #counter for list in list
    total_count=0
    ls_subavg=[]
    ovravg=0
    for i in range(len(ls_ls)):
        subavg=0
        b=0 #counter for subaverage list
        for i in range(len(ls_ls[a])):
            subavg+=ls_ls[a][b]
            b+=1
        ovravg+=subavg
        if subavg == 0:
            subavg == 0.0
        else:
            subavg = subavg/len(ls_ls[a])
        total_count+=len(ls_ls[a])
        ls_subavg.append(subavg)
        a+=1
    ovravg= ovravg/total_count
       
    return ls_subavg, round(ovravg,2)

ans = find_average ([[3 ,4] ,[5 ,6 ,7] ,[ -1 ,2 ,8]])
print(ans)
ans = find_average ([[13.13 ,1.1 ,1.1] ,[] ,[1 ,1 ,0.67]])
print(ans)
ans = find_average ([[3.6] ,[1 ,2 ,3] ,[1 ,1 ,1]])
print(ans)
ans = find_average ([[2 ,3 ,4] ,[2 ,6 ,7] ,[10 ,5 ,15]])
print(ans)



