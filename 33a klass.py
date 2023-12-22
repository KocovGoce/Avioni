class Avioni:
    def avion1():
        s= {
     "prozivodtel":"soko mostar",
      "Tip":"G2-Galeb",
      "namena":"skoslko borben avion"
        }
        print(s)

    def avion2():
        p={
        "prozivoditel":"north america",
        "Tip":"F-86 SAJBER",
        "namena":"locev na avioni",
        "godina na eksplatacija":"1949-1972"
        }
        print(p)# promeliva  za da se aktivra

    def avion3():
       a={
        "prozivoditel":"Republic ",
        "Tip":"F-84 Thunderjet",
        "namena":"locev na avioni",
        "godina na eksplatacija":"1946-1972"
       }
       print(a)
       def f11():
          g={
        "prozivoditel":"Republic ",
        "Tip":"F-84 Thunderjet",
        "namena":"locev na avioni",
        "godina na eksplatacija":"1946-1972"
           }
          print(g)
       

    print("vnesi samo eden od zborovite avion1, avion2, ili avion3, f11\n") 
    k=input('vnesi zbor')#vnesuvanje na od tastaruta za povikuvanje funk1
    if k=='avion1':  #ispituvanje na funkcija 
    
     avion1() #povikuvanje na funkcija vo klasa1
    elif k=='avion2':#pismi elif
      avion2()
    elif k=='avion3':
       avion3()
    elif k=='f11':
        f11()
    else:
       print("pogresno")
     
        

