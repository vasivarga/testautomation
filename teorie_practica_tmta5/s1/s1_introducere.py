"""
################# 1. TERMENI GENERALI #################

Compilare
- executarea/rularea codului scris de catre programator, traducere din ‘human reading syntax’ in ‘machine language’

IDE - Integrated Development Environment (Mediu de Dezvoltare Integrat)
- Este locul in care putem sa scriem si sa rulam cod
- Vine in ajutorul programatorilor avand o serie de functionalitati care fac programarea mai usoara
- Are terminal, consola, venv (in cazul PyCharm)
- Ex: PyCharm (Python), IntelliJ (Java), Visual Studio (C/C++/C#), VSCode(mai multe limbaje), etc

Terminal
- o interfata prin care putem comunica cu sistemul de operare
- de aici putem accesa fisiere, putem rula programe, putem modifica setari
- integrat si cu limbajele de programare/frameworkuri (ex: putem rula programe python direct din terminal)

Consola
- interfata pentru output (rezultatul executarii codului) si input (cand se asteapta input de la user)
- in PyCharm consola se gaseste in partea de stanga-jos, tab-ul denumit "Run"

venv (Virtual Environment)
- Multe programe scrise in Python folosesc librarii externe (bucati de cod/package-uri scrise de altii)
- Aceste librarii pot avea mai multe versiuni (se fac imbunatatiri/adaugari de functionalitati noi)
- Unele versiuni ale librariilor externe pot fi compatibile sau nu cu anumite versiuni de Python
- venv este un mediu virtual care ne ajuta sa izolam aceste versiuni in functie de nevoile pe care le avem pt proiect,
- fiecare proiect Python va avea propriul venv in care se vor putea instala/adauga librarii externe
"""


"""
################# 2. VARIABILE ################# 

- Sunt adrese de memorie la care noi putem sa stocam informatii
- Numele variabilei este de fapt numele adresei de memorie la care sunt stocate informatiile
- Numele variabilelor trebuie sa respecte anumite reguli:
a) trebuie sa inceapa cu litera mica (conventie)
b) nu are voie sa inceapa cu cifra sau caractere speciale (obligatoriu)
c) nu trebuie sa contina spatii (obligatoriu)
d) nu pot fi cuvinte rezervate de Python (obligatoriu), ex: print, False, input
e) numele trebuie sa urmeze formatul camelCase sau snake_case
f) numele variabilelor este case-senstive (adica variabila numepisica nu este egala cu variabila numePisica)
g) numele variabilelor este unic. Daca vom incerca sa facem o redefinire, 
de fapt sistemul nu va aloca o alta adresa de memorie ci va schimba informatia de la adresa de memorie deja alocata
"""

# Formatul textului din punct de vedere al Case Style-ului poate fi:

# a) camelCase - cel mai folosit la numirea variabilelor (mai ales in Java)
# b) snake_case - folosit la numirea variabilelor (mai ales in Python)
# c) PascalCase - folosit la numirea claselor (cam in toate limbajele)
# d) kebab-case - cel mai folosit in url-uri si la numirea endpoint-urilor

# Declarare si initializare variabila:
nume = "Andrei"

'''
In randul de mai sus
1. s-a declarat variabila nume (careia i s-a alocat o zona in memorie)
2. i s-a facut initializarea, adica i s-a atribuit valoarea "Alin"

"Andrei" trebuie scris intre ghilimele pentru a fi considerat text dat de la tastatura si nu numele unei alte variabile
Daca nu era intre ghilimele, sistemul ar fi cautat variabila numita "Andrei". Nu ar fi gasit-o si ar fi returnat eroare
'''

# daca nu folosesc variabila 'nume', ea va fi marcata cu galben ca si atentionare ca nu am folosit continutul anterior
nume = "Andreea"  # momentul in care dau o alta valoare pentru o variabila se numeste suprascriere

print(nume)

prenume, nume, varsta = "Cristi", "Pop", 25
# am facut o dubla declarare si initializare, care este posibil in Python
# am anuntat sistemul ca vrem sa declaram doua variabile, 'prenume' si 'varsta' prin folosirea virgulei
# in dreapta egalului am specificat valorile cu care vrem sa initializam cele doua variabile, in ordinea declararii lor


# Metode "legale" de denumire de variabile (la care compilatorul nu va da eroare):
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Metode ilegale de denumire de variabile (avem eroare la fiecare denumire):
# 2myvar = "John"
# my-var = "John"
# my var = "John"


"""
################# 3. CONSTANTE ################# 
Constantele sunt variabile ale căror valori nu se schimbă în timpul execuției programului. 

Convenții care ne ajuta la definirea și folosirea constantelor:

1. Denumirea cu majuscule
2. Definirea la începutul programului/fisierului
3. Păstrarea valorii variabilei pe tot parcursul programului
"""

PI = 3.14
INSCRIS_LA_CURS = True


"""
################# 4. TIPURI DE DATE ################# 
- Tipul datei precizeaza ce valori poate avea acea data (variabila) și ce operatii se pot face cu ea.

Exista patru tipuri de date primitive in Python:
# string -> au valori de tip text
# int -> au valori numerice intregi (pozitive sau negative)
# boolean -> pot avea doar doua valori: True sau False
# float -> pot stoca numere cu zecimale (adica numere cu virgula)

Tipul de data in python nu este specificat in mod explicit ca in Java/C, ci rezulta din valoarea stocata in variabila
Asta este motivul pentru care putem sa facem schimbare de tip de data

Tipurile de date pe care le facem astazi se numesc tipuri de date primitive/simple.
Mai exista si tipuri de date derivate, dar ele au la baza tot tipuri de date simple.
"""

variabila_string = "Hello world"  # am declarat si initializat o variabila cu tipul de date string
print(variabila_string)
print(type(variabila_string))

# INT (INTREG)
variabila_int = 34
print(variabila_int)
print(type(variabila_int))

# ATENTIE! Aici, daca o pun intre ghilimele este de tip string si nu int:
# variabila_int = "34"

# FLOAT
variabila_float = 3.14  # am declarat si initializat o variabila float. Obs: se foloseste punct (.) nu virgula (,)
print(variabila_float)
print(type(variabila_float))

# ATENTIE! Urmatoarea instructiune nu va stoca o valoare, ci va stoca un tuplu (Curs 3):
# variabila_float_redeclarata = 3,14
# print(variabila_float_redeclarata) # afiseaza un tuplu format din numerele 3 si 14

# BOOLEAN
variabila_boolean_true = True
variabila_boolean_false = False
print(variabila_boolean_true)
print(variabila_boolean_false)
print(type(variabila_boolean_true))
print(type(variabila_boolean_false))

# ATENTIE! Urmatoarea instructiune va da eroare pentru ca va cauta o variabila numita false:
# variabila_boolean_false = false

# ATENTIE! Aici este string si nu boolean:
# variabila_boolean_false = "False"


"""
################# 5. TYPE CASTING ################# 
Type casting se referă la procesul de transformare a unei valori sau a unei expresii de un anumit tip de date 
în alt tip de date.
"""

a = "5"
b = 3

# Daca dorim sa facem suma intre a + b (adica 5+3), trebuie sa convertim string-ul din variabila a intr-un numar intreg,
# altfel avem eroare
print(int(a) + b)

# Daca dorim sa lipim textul a de textul b (adica 53), trebuie sa convertim nr-ul intreg din variabila b intr-un numar
# string, altfel avem eroare
print(a + str(b))
