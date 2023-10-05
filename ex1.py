num = int(input("Digite um número: "))
match num:
    case 1:
        print("Este é o número 1")
    case 2:
        print("Este é o número 2")
    case 3:
        print("Este é o número 3")
    case _:
        print("Outro número")