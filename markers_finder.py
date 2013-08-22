# coding: utf-8

import sys


def underscore(wejscie):
	return "<u>" + wejscie + "</u>"

def wykrywaj(ciag, sekwencja_pocz, sekwencja_konc):
	zazn_poczatek = "<span style='background-color: yellow;'>"
	zazn_koniec = "</span>"
	pozycja_pocz = ciag.index(sekwencja_pocz)
	pozycja_konc = ciag.index(sekwencja_konc)
	return ciag[0:pozycja_pocz] + zazn_poczatek + underscore(sekwencja_pocz) + ciag[pozycja_pocz+len(sekwencja_pocz):pozycja_konc] +  underscore(sekwencja_konc) +  zazn_koniec +  ciag[pozycja_konc+len(sekwencja_konc) : ]

parametr_pocz = sys.argv[1]
parametr_konc = sys.argv[2]

plik = open("sekwencja.txt", "r")
dane = plik.read()
zwrotka = "<html><head></head><body><div style='font-size:15px;width:800px;word-wrap:break-word;'>"
zwrotka += wykrywaj(dane, parametr_pocz, parametr_konc)
zwrotka += "</div></body></html>"
plik_wyjsciowy = open("sekwencja.html", "w")
plik_wyjsciowy.write(zwrotka)
plik_wyjsciowy.close()



