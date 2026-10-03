
# only 0 - 100, so use simple conditions

def convert_smalls(cislo):
# 1 to 19
    if cislo == 1:
        return "jedna"
    elif cislo == 2:
        return "dva"
    elif cislo == 3:
        return "tři"
    elif cislo == 4:
        return "čtyři"
    elif cislo == 5:
        return "pět"
    elif cislo == 6:
        return "šest"
    elif cislo == 7:
        return "sedm"
    elif cislo == 8:
        return "osm"
    elif cislo == 9:
        return "devět"
    elif cislo == 10:
        return "deset"
    elif cislo == 11:
        return "jedenáct"
    elif cislo == 12:
        return "dvanáct"
    elif cislo == 13:
        return "třináct"
    elif cislo == 14:
        return "čtrnáct"
    elif cislo == 15:
        return "patnáct"
    elif cislo == 16:
        return "šestnáct"
    elif cislo == 17:
        return "sedmnáct"
    elif cislo == 18:
        return "osmnáct"
    elif cislo == 19:
        return "devatenáct"
    else:
        return ""

def convert_tens(cislo):
# 2 to 9
    if cislo == 2:
        return "dvacet"
    elif cislo == 3:
        return "třicet"
    elif cislo == 4:
        return "čtyřicet"
    elif cislo == 5:
        return "padesát"
    elif cislo == 6:
        return "šedesát"
    elif cislo == 7:
        return "sedmdesát"
    elif cislo == 8:
        return "osmdesát"
    elif cislo == 9:
        return "devadesát"
    else:
        return ""

def cislo_text(cislo):

    try:
        int_value = int(cislo)
    except ValueError:
        return f"Neplatné číslo: {cislo}"

    if int_value < 0 or int_value > 100:
        return f"Číslo {cislo} musí být v rozsahu 0-100"
    elif int_value == 0:
        return "nula"
    elif int_value == 100:
        return "sto"
    elif int_value < 20:
        return convert_smalls(int_value)
    else:
        smalls = int_value % 10
        tens = int_value // 10
        if smalls == 0:
            return convert_tens(tens)
        return convert_tens(tens) + " " + convert_smalls(smalls)

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)