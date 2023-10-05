dia = str(input("Digite o Dia: "))
match dia:
    case("Segunda"|"Terça"|"Quarta"|"Quinta"|"Sexta"):
        print(f"{dia} é um dia util")
    case("Sabado"|"Domingo"):
        print(f"{dia} não é um dia util")