#print ("hoje choveu")

"""comentario de multiplas 
linhas usando strigs"""

'''comentario de multiplas 
linhas usando strigs, pode ser simples ou duplas'''

##variavel do tipo inteiro
#idade = 25

#variavel do tipo string
#nome = "romario"

# variavel do tipo float
#altura = 1.75

#variavel dp tipo bool
#estudante = True

#print(f"meu nome é",{nome}, "idade", {idade}, "e altura", {altura})

#conta quantas letras tem no mensagem
#mensagem = "João vitor veroneze"
#print(len(mensagem))


#mostra qual tipo de variavel
#x=10
#print(type(x)) 

#y=3.14
#print(type(y))

#print(type(nome))

#professor=False
#print(type(professor))


#pede o nome e depois fala o nome dizendo ola
#nome = input("qual é seu nome? ")
#print( "ola, "+ nome + "!")

'''conversao de numeros '''

#numero_float = 42.9
#numero_inteiro = int(numero_float)
#print(f"conversao de (numero_float) para inteiro: {numero_inteiro}")

#numero_string = "123"
#numero_inteiro = int (numero_string)
#print (f"conversao de (numero_string) para numero {numero_inteiro}")
#print(f"o tipo de variavel numero_inteiro E {type(numero_inteiro)}")

#numero_string_float = "123.456"
#numero_float = float(numero_string_float)
#print (f"conversao de {numero_string_float} para numero {numero_float}")
#print(f"o tipo de variavel numero_inteiro E {type(numero_float)}")
#print(numero_float + 1)

#numero_inteiro = 456
#numero_string = str(numero_inteiro)
#print(f"conversao de {numero_inteiro} para string {numero_string}")
#print(f"o tipo de variavel numero_string e {type(numero_string)}")

#numero_float = 456.789
#numero_string_float = str(numero_float)
#print(f"conversao de {numero_float} para string {numero_string_float}")
#print(f"o tipo de variavel numero_string_float e {type(numero_string_float)}")

#numero = int (input("digite um numero "))
#print (f"o numero vale {numero} e o seu tipo é {type(numero)}")
#print(f"a soma de",numero, "+ 1  " )
#print(f"é { numero + 1 }")

'''divisao de ponto fracionario'''

#X = 22
#y = 7
#resultado_divisao_inteira = X // y
#print (f"divisao inteira {X} // {y} = {resultado_divisao_inteira}")

'''resto'''

#X = 22
#y = 7
#resultado_divisao_inteira = X % y
#print (f"o resto de  {X} e {y} = {resultado_divisao_inteira}")

"""potencia"""

#X = 2
#y = 8
#resultado_divisao_inteira = X ** y
#print (f"o resto de  {X} ** {y} = {resultado_divisao_inteira}")

'''exercicios'''

'''att1'''

#nro = float(input("digite um numero: "))
#nro2 = float(input("digite um segundo numero: "))
#soma = nro + nro2
#print("a soma entre ",nro, "e", nro2, "é", soma)

'''att2'''

#nro = input("digite um numero: ")
#numero_inteiro = int(nro)
#dobro = numero_inteiro * 2
#print(f"o dobro de ",numero_inteiro, "é", dobro)

'''att3'''

#nro = float(input("digite um numero: "))
#nro2 = float(input("digite um segundo numero: "))
#nroINT= int(nro)
#nroINT2= int(nro2)
#mult = nroINT* nroINT2
#print("a multiplicação entre ",nroINT, "e", nroINT2, "é", mult)

'''att4'''

#altura = int(input("digite a altura do retangulo"))
#base = int(input("digite a base do retangulo"))
#area = altura * base
#print (F"a area do retangulo é {area}")

'''att5'''

#celsius = float(input("digite uma temperatura em Celsius "))
#f=((9/5)*celsius + 32)
#print(F"a temperatura {celsius}em graus celsisus é {f} em Fahrenheit")


'''atividades aula 03/10/24'''

''' aspas'''

#mesagem1 = "ola mundo"

#mesagem2 = 'ola mundo'

#mensagem3 = "ola 'mundo'"

#mensagem4 = 'ola "mundo"'

#print (mensagem1)

'''junçao de string'''

#nome= "ana"
#sobrenome = "silva"
#nome_completo = nome + " " + sobrenome
#print(nome_completo)

'''SLINCE'''

#texto = "hello"
#print(texto[:3]) #SAIDA: HEL
#print(texto[3:]) #SAIDA: LO
#print(texto[:4]) #SAIDA: HELL
#print(texto[2:-1]) #SAIDA: LL
#print(texto[:-2]) #SAIDA: HEl

"""upper"""

#deixa em maiusculo
#texto= "python"
#print(texto.upper())
#saida: PYTHON

"""capitalize"""

#deixa a primeira letra em maiusculo
#texto = "python programing"
#print (texto.capitalize())

"""title"""
'''deixa as primeiras letras em mausculo'''

#texto = "python programing language"
#print (texto.title())

"""att 1"""
#nome = input("digite seu nome: ")
#sobrenome = input ("digite seu sobrenome: ")
#nome_completo= nome + " " +sobrenome
#print(nome_completo)

"""att2"""

#frase= input("escreva uma frase: ")
#print(frase[:4],len(frase))

"""att3"""

#frase= input("escreva uma frase: ")
#print(frase.capitalize())
#print(frase.title())
#print(frase.upper())

"""......................................"""

"""att1"""

#nota1= float (input("digite sua primeira nota : "))
#nota2= float (input("digite sua segunda nota: "))
#nota3= float (input("digite sua terceira nota "))
#media = (nota1 + nota2 + nota3) / 3
#print(f"sua media é de: {media}")

''''att2'''

#tempo= int(input("digite um tempo em ninutos: "))
#segundos = tempo * 60
#print(f"seu tempo em segundos é {segundos}")

"""att3"""

#tempo= float (input("digite o tempo da viagem: "))
#distancia= float (input ("digite o distancia percorrida: "))
#t=tempo/60
#velocidade_media= distancia/t
#print(f"o velociade media é de {velocidade_media}")

'''att4'''

#preco= float(input("digite o preço: "))
#desconto= float(input("qual a porcentagem do desconto: "))
#porcent_desconto= preco * (desconto/100)
#final= preco - porcent_desconto
#print(f"o preco com desconto é de {final}")

"""att5"""

#peso= float(input("digite seu peso: "))
#altura= float(input("digite sus altura"))
#imc=peso/(altura*altura)
#print(f" seu IMC é de {imc}")


'''verifica se os dois valores sao iguais'''

#x = 10
#y = 10
#z = 11
#print(x==y)  #true
#print(x==z)  #false

"""diferente"""
#x = 10
#y = 10
#z = 11
#print(x!=y)  #false
#print(x!=z)  #true

'''verificar se é maior'''

#x > 10
#y > 10
#z > 11
#print(x > y)  #false
#print(z > x)  #true


"""inversor"""
"""retorna false seo resultado for true e true se for false"""

#a = True
#b = False
#print(a==b)  #false
#print(not a==b)  #true

"""ou (or)"""

"""retorna true se uma das afirmaçoes for verdadeiras"""

#x = True
#y = False

#print(x or y) # true


"""e (and)"""
"""retorna true se ambas as afirmaçoes fores verdadeiras"""

#x = True
#y = False
#print( x and y)  # false
#print (x and x ) #true


"""atividades"""

#numero = int(input("digite um numero: "))
#print(numero<0)


"""att2"""

#idade = int(input("Digitte sua idade: "))

#print(f"pode vatar: {idade>=16}")
#print(f"pode dirigir: {idade>=18}")

"""att3"""

usuario = input("digite seu usuario: ")
senha = int(input("digite sua senha: "))

print(f"usuario conctado {usuario == "admin"  or usuario == "user" and senha == 1234} ")

#x = 10
#if x > 0:
 #   print("x é positivo")
#print("fim do programa")   


#x=10
#if x > 0:
 #   print("x é positivo")
#elif x ==  0:
#    print("x= zero") 
#print("fim programa")  


#x = 10 

#if x > 0:
   # print("x é positivo")
#elif x == 0:
    #print("x é zero")
#else:
   # print ("x é negativo")        

"""atividade"""

#media = float(input(" digite sua media: "))

#if media>=7:
   # print (f"aluno aprovado {media}")
#elif media>=5:
   # print(f"aluno deve prestar exame: {media}")    
#else:
    #print(f"aluno reprovado: {media}")