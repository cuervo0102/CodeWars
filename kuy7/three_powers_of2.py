def three_powers(n):
    powers = []
    i = 0
    while 2 ** i <= n :
        powers.append(2**i)
        i += 1 


    for i in range(len(powers)):
        for j in range(i+1, len(powers)):
            for k in range(j+1, len(powers)): 
                sum = powers[i] + powers[j] + powers[k]
                if sum == n : 

                    return True
                

    

    return False

print(three_powers(2))