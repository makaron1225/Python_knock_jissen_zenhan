def i(n):
    return "3" in str(n)


count = 0
n = 1

while count < 100:
    if i(n):
        print(n)
        count += 1
    n += 1


num = 1
count = 0
while count < 100:
    if "3" in str(num):
        print(num)
        count += 1
    num += 1
