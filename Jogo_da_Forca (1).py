import random

# Modelo da Forca (Professora passou, desenhos)

des_forca = ['''
 \t\t\t +---+
 \t\t\t |   |
 \t\t\t     |
 \t\t\t     |
 \t\t\t     |
 \t\t\t     |    
 \t\t\t =========''', '''
 \t\t\t +---+
 \t\t\t |   |
 \t\t\t O   |
 \t\t\t     |
 \t\t\t     |
 \t\t\t     |    
 \t\t\t =========''', '''
 \t\t\t +---+
 \t\t\t |   |
 \t\t\t O   |
 \t\t\t |   |
 \t\t\t     |
 \t\t\t     |    
 \t\t\t =========''', '''
 \t\t\t +---+
 \t\t\t |   |
 \t\t\t O   |
 \t\t\t/|   |
 \t\t\t     |
 \t\t\t     |    
 \t\t\t =========''', '''
 \t\t\t +---+
 \t\t\t |   |
 \t\t\t O   |
 \t\t\t/|\  |
 \t\t\t     |
 \t\t\t     |    
 \t\t\t =========''', '''
 \t\t\t +---+
 \t\t\t |   |
 \t\t\t O   |
 \t\t\t/|\  |
 \t\t\t/    |
 \t\t\t     |    
 \t\t\t=========''', '''
 \t\t\t +---+
 \t\t\t |   |
 \t\t\t O   |
 \t\t\t/|\  |
 \t\t\t/ \  |
 \t\t\t     |    
 \t\t\t=========
''']

print('-------------- Jogo da Forca --------------\n\n')

num = 1

while num > 0:
  vet = []
  count = 0
  des = 0
  letras_ditas = []

  num = int(input("--- Escolha o tipo de lista para jogar! ---\n\n1 - Animais\n2 - Frutas\n\n"))

  #Biblioteca de tipos:
  lista_animais = ["leao", "macaco", "cachorro", "lagarto", "foca", "golfinho", "elefante"]
  lista_frutas = ["banana", "maça", "pessego", "manga", "amora", "ameixa", "acerola", "laranja", "limao"]

  #Biblioteca de animais:
  if num == 1:
    pos = random.randint(0,len(lista_animais)-1)
    palavra_sorteada = lista_animais[pos]
    print(des_forca[0])
    print("\n")

    print(end="\t\t\t")

    for i in range(0, len(palavra_sorteada),1):
      vet.append('_')
      print(vet[i], end=' ')
    
    print("\n")

    while count != len(palavra_sorteada) and des != 6:
      letra = '1'

      while (ord(letra) >= 65 and ord(letra) <= 90 or ord(letra) >= 97 and ord(letra) <= 122) == False:
        letra = input("\nAdivinhe a palavra. Digite uma letra: \n")
        if ord(letra) >= 65 and ord(letra) <= 90 or ord(letra) >= 97 and ord(letra) <= 122:
          if ord(letra) >= 65 and ord(letra) <= 90:
           letra = letra.lower()
          else:
           print("Dígito inválido !")

      count_letras = 0

      for i in range(0,len(letras_ditas),1):
        if letra == letras_ditas[i]:
          count_letras+=1

      if count_letras > 0:
        print("\nLetra já foi dita anteriormente.\n")
      else:
        aux = count

        for i in range(0,len(palavra_sorteada),1):

          if letra == palavra_sorteada[i]:
            vet[i] = letra
            letras_ditas.append(letra)
            count+=1
          else:
            letras_ditas.append(letra)
        
        if aux == count:
          des+=1

        print("\n")
        print(des_forca[des])
        print("\n")

        for i in range(0,len(palavra_sorteada),1):  
          print(vet[i], end=' ')
        print("\n")

  #Biblioteca de frutas:

  elif num == 2:
    pos = random.randint(0,len(lista_frutas)-1)
    palavra_sorteada = lista_frutas[pos]
    print(des_forca[0])
    print("\n")

    print(end="\t\t\t ")

    for i in range(0, len(palavra_sorteada),1):
      vet.append('_')
      print(vet[i], end=' ')
    
    print("\n")
    
    while count != len(palavra_sorteada) and des != 6:
      letra = '1'

      while (ord(letra) >= 65 and ord(letra) <= 90 or ord(letra) >= 97 and ord(letra) <= 122) == False:
        letra = input("\nAdivinhe a palavra. Digite uma letra: \n")
        if ord(letra) >= 65 and ord(letra) <= 90 or ord(letra) >= 97 and ord(letra) <= 122:
          if ord(letra) >= 65 and ord(letra) <= 90:
           letra = letra.lower()
          else:
           print("Dígito inválido !")
      count_letras = 0
  
      for i in range(0,len(letras_ditas),1):
        if letra == letras_ditas[i]:
          count_letras+=1

      if count_letras > 0:
        print("\nLetra já foi dita anteriormente.\n")
      else:
        aux = count

        for i in range(0,len(palavra_sorteada),1):
          if letra == palavra_sorteada[i]:
            vet[i] = letra
            letras_ditas.append(letra)
            count+=1
          else:
            letras_ditas.append(letra)
        
        if aux == count:
          des+=1

        print("\n")
        print(des_forca[des])
        print("\n")

        for i in range(0,len(palavra_sorteada),1):  
          print(vet[i], end=' ')
        print("\n")

  #Se quiser adicionar nova biblioteca, podemos adicionar.

  if count >= len(palavra_sorteada):
    print("Parabéns! Você acertou a palavra!\n")
  
  if des >= 6:
    print("Poxa! Você esgotou suas tentativas!\n")

  print("\n")
  num = int(input("---------- Para jogar novamente: ----------\n\n1 - Sim\n0 - Não\n\n"))