#Zadanie 1

# licz = 0
# lista_podstawowa = []
# while licz < 9:
#     lista_podstawowa.append(int(input("Type number ")))
#     licz += 1
# lista1 = sorted(lista_podstawowa)
# lista2 = lista1[::-1]
# lista3 = []
# n = int(input("How many numbers in list "))
# i = 0
# suma = 0
# if n < len(lista2):
#     while i < n:
#         lista3.append(lista2[i])
#         suma = suma + lista2[i]
#         i += 1
#     print(lista3)
#     print(suma)
# else :
#     print("Za dużo pan napisał")



#Zadanie 2

# def czy_proste(number):
#     if int(number) < 2 :
#         return False
#     for dziel in range(2, int(number)):
#         if int(number) % dziel == 0:
#             return False
#     else:
#         return True
# def find_proste(n):
#     nyz = int(n) - 1
#     ver = int(n) + 1
#     while True:
#         if int(n) < 2 :
#             return 2
#         if czy_proste(nyz):
#             return nyz
#         if czy_proste(ver):
#             return ver
#         else:
#             nyz -= 1
#             ver += 1
# a = input("Type your number ")
# c2 = find_proste(a)
# print("Nearest prime number is", c2)
# print("Suma liczb parzystych to", sum(int(digit) for digit in str(c2) if int(digit) % 2 == 0))



#Zadanie 3

# def czy_proste(number):
#     if int(number) < 2 :
#         return False
#     for dziel in range(2, int(number)):
#         if int(number) % dziel == 0:
#             return False
#     else:
#         return True
# a = input("Choose your number ")
# if czy_proste(a):
#     b = str(a)[::-1]
#     if czy_proste(b):
#         print(b, "To liczba pierwsza")
#     if not czy_proste(b):
#         print(b, "To nie liczba pierwsza")
# else :
#     print(a, "To nie liczba pierwsza")