import urllib.request
import json
import sys


def getRateValute(izValute, uValutu):
    URL = f'={izValute}&to={uValutu}'

    try:
        odgovor = urllib.request.urlopen(URL).read()
        recnik = json.loads(odgovor)
        if 'result' not in recnik:
            print("Greška: Ključ 'result' nije pronađen u odgovoru API-a.")
            sys.exit(1)
        faktor = recnik['result']
        return float(faktor)
    except Exception as e:
        print(f"Greška prilikom dobijanja informacija o valutama: {e}")
        sys.exit(1)


def ucitajValutu(pitanje):
    while True:
        valuta = input(pitanje).upper()
        if valuta:
            return valuta
        else:
            print('Unos ne može biti prazan.')


print("Program računa koeficijent konverzije između dve valute.")

izValute = ucitajValutu('\nUnesite početnu valutu (primer: USD): ')
iznos = float(input(f'\nUnesite iznos za konverziju ({izValute}): '))
uValutu = ucitajValutu('\nUnesite ciljnu valutu (primer: EUR): ')

faktorKonverzije = getRateValute(izValute, uValutu)
konvertovaniIznos = iznos * faktorKonverzije

print(f'\nKoeficijent konverzije: {izValute} u {uValutu} je: {faktorKonverzije}')
print(f'Iznos {iznos} {izValute} u {uValutu} je: {konvertovaniIznos} {uValutu}')
print()

sys.exit()
