def process_scores(f):
    total = 0
    data = f.read()
    data_list = data.split()
    length = len(data_list)
    for idx in range(length):
        total+=float(data_list[idx])
    avg = total/length
    return(total, avg)
    
f = open("scores.txt", "r")
ans = process_scores(f)
print("Output: ",ans)
