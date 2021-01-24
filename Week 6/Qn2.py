def check_password(pw):
    length = len(pw)
    if length < 8 or not pw.isalnum() or count_digit(pw) < 2:
        return False
    else:
        return True

def count_digit(pw):
    count = 0
    for num in range(len(pw)):
        if pw[num].isdigit():
            count+=1
    return count

print("check_password('test')")
ans = check_password('test')
print(ans)
print("check_password('testtest')")
ans = check_password('testtest')
print(ans)
print("check_password('testt22')")
ans = check_password('testt22')
print(ans)
print("check_password('testte22')")
ans = check_password('testte22')
print(ans)
