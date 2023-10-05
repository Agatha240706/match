login = str(input('informe se login: '))
senha = str(input('informe sua senha: '))

match (login,senha):
    case ("admin", "admin_pass"):
        print('bem-vindo admin')
    case ("user", "user_pass"):
        print('bem-vindo user')
    case ("guest", _):
        print('bem-vindo guest')
    case _:
        print('erro ao logar')