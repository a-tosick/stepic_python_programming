p = int(input())
if p == 1:
    print(p, "программист")
elif 2 <= p <= 4:
    print(p, "программиста")
elif 5 <= p <= 20:
    print(p, "программистов")
elif 11 <= (p % 100) <= 19:
    print(p, "программистов")
elif (p % 10) == 1:
    print(p, "программист")
elif 2 <= (p % 10) <= 4:
    print(p, "программиста")
else:
    print(p, "программистов")