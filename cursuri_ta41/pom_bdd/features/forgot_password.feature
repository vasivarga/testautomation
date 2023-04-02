#Feature: Forgot pass page
#
##  Background: Login page to be opened
##  Given Login page: I am on the Login page
#
#  """
#  Background este o modalitate prin care putem sa dam un context general testelor noastre (nu functioneaza
#  decat cu GIVEN)
#  Putem sa punem in background orice elemente de context care sunt valabile pentru toate scenariile din feature file
#  Daca vrem sa separam testele pe care le rulam pentru rulare individuala putem sa ne folosim de conceptul de tag-uri
#  Tag-urile incep cu semnul @ si sunt urmate de free text (recomandat sa fie ceva sugestiv pentru scenariul in scop
#  Un scenariu poate sa fie identificat de mai multe tag-uri
#  In momentul rularii putem sa specificam tag-ul care ne intereseaza si se vor rula toate testele identificate de acel tag
#  Scenario outline = o modalitate prin care putem sa rulam acelasi test de mai multe ori cu mai multe perechi
#                        de valori de input
#  """