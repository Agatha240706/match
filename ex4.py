anml = str(input("Digite um animal: "))
match anml:
    case ("vaca") :
        print("É vaca")
    case ("galinha"):
        print("É galinha")
    case ("ovelha"):
        print("É ovelha")
    case _ :
        print("Animal desconhecido")