prime_numbers = []
for i in range(1,100):
    if i > 1 :
        for k in range(2,i):
            if i % k == 0:
                break
        else :
            prime_numbers.append(i) # birden yüze kadar olan asal sayıları yazma
print(prime_numbers)                #else neden orda ?