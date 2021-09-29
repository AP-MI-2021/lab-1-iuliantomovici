'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
    if n < 2:
      return False
    for divizor in range(2, n):
      if n % divizor == 0:
        return False
    return True
  #nu stiu cum implementez biblioteca pentru a face n/2, multumesc
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  produs=1
  for numar in lst:
    produs=produs*numar
  return produs

  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  while  x!=y:
    if x>y:
      x=x-y
    else:
      y=y-x
  return y

'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  rest = x % y
  while rest != 0:
    x = y
    y = rest
    rest = x % y
  return y
  
  
def main():
  # interfata de tip consola aici
  n = int(input("Dati posibilul numar prim:"))
  print(is_prime(n))

  lst = []
  number_of_elements = int(input("Introduceti numarul de elemente ale listei:"))
  for i in range(0,number_of_elements):
    number = int(input("Introduceti element:"))
    lst.append(number)
  print(get_product(lst))
  x=int(input("Introduceti primul numar"))
  y=int(input("introduceti aldoilea numar"))
  print("Cel mai mare divizor comun al celor doua numere este",get_cmmdc_v1(x,y))
  print(get_cmmdc_v2(6,9))
if __name__ == '__main__':
  main()
