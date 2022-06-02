# pessoa_v7.py

class Pessoa:
    def __init__(self, nome, login=False, logoff=False) -> None:
        self.nome = nome
        self.login = login
        self.logoff = logoff

    def logar(self):
        if self.login:
            print(f'{self.nome}, já está logado no sustema.!')
            return
        print(f'Seja bem vindo {self.nome}, você está logado no sustema.!')    
        self.login = True

    def deslogar(self):
        if not self.login:
            print(f'{self.nome} não está logado no sistema!')
            return
        print(f'{self.nome} foi deslogado do sistema!')    
        self.login = False

usuario = Pessoa('Adriano')
print(usuario.login)

usuario.logar()
usuario.logar()
print(usuario.login)
usuario.deslogar()
usuario.deslogar()
print(usuario.login)