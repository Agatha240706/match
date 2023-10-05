Cor = str(input("Escolha uma cor: "))
match Cor:
    case ("vermelho") :
        print("É vermelho")
    case ("azul"):
        print("É azul")
    case ("verde"):
        print("É verde")
    case _ :
        print("É outra cor")