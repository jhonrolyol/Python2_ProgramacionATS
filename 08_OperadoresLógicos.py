"""
                      PROGRAMACIÓN ATS
 Topic: Operadores Lógicos
 Author: J.R.
 Date: october 01, 2022
 Vídeo: https://www.youtube.com/watch?v=ZjeOT_ACdhw&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=8
"""

'''
- Permite construir expresiones lógicas, se obtiene como resultado booleanos.

  And (Conjunción)  ----- and
  Or (Disyunción)    ----- or
  Negación           ----- not

'''
# Operador AND:
'''
 Operador 1 | Operador | Operador 2 | Resultado 
    True        and          True       True
    True        and          False      False
    False       and          True       False
    False       and          False      False
'''

# Operador OR:
'''
 Operador 1 | Operador | Operador 2 | Resultado 
    True         or          True       True
    True         or          False      True
    False        or          True       True
    False        or          False      False
'''
# Iperador Negación:
'''
    Operando     |  resultado
    not(True)         False
    not(False)        True
'''
# Priporidad de los operadores lógicos
'''
1.- not
2.- and
3.- or

# Ejemplo:
a = 10; b = 12; c = 13; d = 10;
((a>b)) or (a<c) and ((a==c) or (a>=b))
  F     or    T          F   or    F
        T        and         F
                  F
'''
# Priporidad de los operadores en general
'''
1.- ()
2.- **
3.- *,/,mod,not
4.- +,-, and
5.- >,<,==,>=,<=,!=,or
'''

# Aplicación:
a=10
b=15
c=20
resultado1 = ((a<b) and (b<c))
print(resultado1)

resultado2 = ((a>b) and (b<c))
print(resultado2)

resultado3 = ((a>b) or (b<c))
print(resultado3)


resultado4 = not((a>b) or (b<c))
print(resultado4)

