from utilities import unos_realnog_pozitivnog_broja, unos_intervala
from .automobil import Automobil
from .stan import Stan
from .instrukcije import Instrukcije

def unos_artikla(redni_broj):

    naslov = input(f'Unesite naslov {redni_broj}. artikla: ')
    opis = input(f'Unesite opis {redni_broj}. artikla: ')
    cijena = unos_realnog_pozitivnog_broja(f'Unesite cijenu {redni_broj}. artikla: ')

    print('Tipovi artikla: ')
    print('\t1. Stan')
    print('\t2. Automobil')
    print('\t3. Instrukcije')

    tip_artikla = unos_intervala(1,3)

    if tip_artikla == 1:
        kvadratura = unos_realnog_pozitivnog_broja(f'Unesite kvadraturu {redni_broj}. stana: ')

        return Stan(kvadratura, naslov, opis, cijena)

    elif tip_artikla == 2:
        snaga = unos_realnog_pozitivnog_broja(f'Unesite snagu {redni_broj}. auta: ')

        return Automobil(snaga, naslov, opis, cijena)

    elif tip_artikla == 3:

        return Instrukcije(naslov, opis, cijena)