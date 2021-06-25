'''
variaveis
'''
# name= "Geovany"
# print (name)
# ========================

# a=b=c= "cat"
# print (a)
# print (b)
# print (c)

# ================
# reusar nomes de variaveis, ele escreve sempre o ultimo valor atribuido, apaga o primeiro 

# color= "blue"
# color= "red"
# print(color)

# =================

# Nomes aceitos para variaveis
# aceita maiusculas, minusculas, mistura, letras com numero no fim,separado por underscore

# ===========

# Nomes nao aceitos para variaveis
# separado por espaco, separado por traco,letra com numero no inicio

# Nomes reservados, que nao se pode usar

# help ("keywords")
# from= "london"

# ===========================
# Tipos de variveis

# var= "Hello world"
# print (type(var))

# var=23
# print (type(var))


'''
Identidade de objetos 
'''

# score = 400
# identity=(id(score))
# print(identity)

# =======================


# score = 400
# pb = score
# print (id(score))
# print (id(pb))

# ===============

# Referencia de objectos
# pb--------------------> int 20
# score-----------------> int 100
# pb=20
# score=100

# print(type(score))
# print (type(pb))
# print (score)
# print (pb)


# ==================

# garbage collection
# pb------------------->int 20
# score----------------->int100
# score-----------------str cheio
pb=20
score=100
score="hoje"

print(type(score))
print (type(pb))
print (score)
print (pb)