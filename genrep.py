#Author: David Ljubicic
#Date: 2025-10-07

print("\nEi24 - genrep praktiskt prov ht25")

nummer = input("Ange resistorer: ").strip()

if nummer == "0" or nummer == "":
    print("Serieresistans: 0")
    print("Parallellresistans: 0")

else:
    serie = list(map(int, nummer.split()))
    parallell = sum(1/x for x in serie)
    print(f"Serieresistans: {sum(serie)}")
    print(f"Parallellresistans: {(1/parallell)} \n")
