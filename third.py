
def je_prvocislo(cislo):
    
    cislo = int(cislo)
    if cislo <= 1:
        return False
    elif cislo <= 3:
        return True
    # Not optimised but works fine
    for delitel in range(2, int(cislo**0.5) + 1):
        if cislo % delitel == 0:
            return False
    return True
2
def vrat_prvocisla(maximum):

    maximum = int(maximum)
    results = []
    for i in range(1, maximum + 1):
        if je_prvocislo(i):
            results.append(i)
    return results

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    print(je_prvocislo(cislo))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)