student1 = (145881,"Cezary","Dobreńko")
student2 = (145882,"Marcin","Gałązka")
student3 = (145883,"Patryk","Konopko")
student4 = (145884,"Artur","Dymkowski")
student5 = (145885,"Zygmunt","Hajzer")
lista_studentow = [student1,student2,student3,student4,student5]


slownik = dict([
  (student1[0], {"imie": student1[1],"nazwisko": student1[2],"wiek": 22, "email":"c.dobrenko@op.pl","rok urodzenia":1997,"adres":"Brejdyny 59"}),
  (student2[0], {"imie": student2[1],"nazwisko": student2[2],"wiek": 21, "email":"e.dobrenko@op.pl","rok urodzenia":1996,"adres":"Brejdyny 58"}),
  (student3[0], {"imie": student3[1],"nazwisko": student3[2],"wiek": 20, "email":"z.dobrenko@op.pl","rok urodzenia":1995,"adres":"Brejdyny 57"}),

])

print(slownik[145883]["nazwisko"])