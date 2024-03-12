def functional(n):
    ret = 0
    if n < 0 or n > 20:
        print("argment is under 0 or orver 20")
        return ret
    int = n
    for num in range(n):
        if num == 0:
            ret = int
            int = int - 1
            continue
        ret = ret * int
        int = int - 1
    return ret
    
print(functional(15))