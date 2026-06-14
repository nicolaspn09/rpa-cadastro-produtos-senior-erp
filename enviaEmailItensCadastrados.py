import sys
from collections import defaultdict

sys.path.append(r"C:\rpa\Python")

from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer
from Classes.Hangouts.Hangouts.Hangouts import Hangouts



class EnviaEmailItensCadastrados:
    def __init__(self):
        pass # Logica de negocio removida por seguranca corporativa


    def consulta_tabela_itens_cadastrados():
        pass # Logica de negocio removida por seguranca corporativa



    def atualiza_status_itens_cadastrados(codigo_produto):
        pass # Logica de negocio removida por seguranca corporativa



    def envia_email_itens_cadastrados(tabela):
        pass # Logica de negocio removida por seguranca corporativa

    


if __name__ == "__main__":
    tabela = EnviaEmailItensCadastrados.consulta_tabela_itens_cadastrados()
    EnviaEmailItensCadastrados.envia_email_itens_cadastrados(tabela)