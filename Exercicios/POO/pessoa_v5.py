# pessoa_v5.py

class Pessoa:
    def __init__(self, nome, login=False, logoff=False) -> None:
        self.nome = nome
        self.login = login
        self.logoff = logoff

    def logar(self):
        print(f'Seja bem vindo {self.nome}, você está logado no sustema.!')
        self.login = True

usuario = Pessoa('Adriano')
print(usuario.login)

usuario.logar()
print(usuario.login)
