number = int(input("Number to check: "))
# we need the length of number
l = len(str(number))
total = 0

a = number
while a > 0:
    digit = a % 10
    total += digit**l
    a //= 10
# Hosgeldin Yasin abi.Burayı değiştir.
# lets print the result
# Sunday Meeting
if number == total:
    print(number, "is an Armstrong number!")
else:
    print(number, "is not an Armstrong number!")


# viveriveniversum @ github ------C7208-Onur MANAP
