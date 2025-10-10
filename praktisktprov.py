#Author: David Ljubicic
#Date: 2025-10-10

r_string = input("Vilka tabeller vill du beräkna? ")

if r_string == "":
    print("0")
else:
    r_list = r_string.split()
    r_int = [int(i) for i in r_list]

    for num in r_int:
        print(f"\nMultiplikationstabell för {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")