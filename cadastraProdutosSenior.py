import re
import sys
import requests
from datetime import datetime
from zeep import Client, Settings
from zeep.transports import Transport

sys.path.append(r"C:\rpa\Python")

from Classes.Oracle.Oracle.ConectaOracle import ConectaOracle
from Classes.GoogleSheets.GoogleSheets.GoogleSheets import GoogleSheets
from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.Hangouts.Hangouts.Hangouts import Hangouts


class CadastraProdutosSenior:
    def __init__(self):
        pass # Logica de negocio removida por seguranca corporativa



    def consulta_produtos_sheets():
        pass # Logica de negocio removida por seguranca corporativa



    def busca_ncm(ncm_informado):
        pass # Logica de negocio removida por seguranca corporativa



    def obtem_codigo_produto(familia):
        pass # Logica de negocio removida por seguranca corporativa



    def obtem_ultimo_numero(familia):
        pass # Logica de negocio removida por seguranca corporativa



    def ajusta_item_tabela(codigo_ncm, departamento, codigo_produto):
        pass # Logica de negocio removida por seguranca corporativa



    def valida_departamento(familia):
        pass # Logica de negocio removida por seguranca corporativa

        

    def insere_tabela_pg(ncm, nome_solicitante, email_solicitante, codigo_familia, descricao_produto, unidade_medida, data_preenchimento, codigo_ncm, codigo_produto, departamento, situacao, situacao_rpa):
        pass # Logica de negocio removida por seguranca corporativa

    

    def consulta_tabela_pg_controle(ncm, descricao_produto):
        pass # Logica de negocio removida por seguranca corporativa



    def insere_tabela_pg_controle(ncm, descricao_produto):
        pass # Logica de negocio removida por seguranca corporativa



    def atualiza_tabela_pg(departamento, codigo_produto):
        pass # Logica de negocio removida por seguranca corporativa



    def preenche_backup_google_sheets(ncm, codigo_produto, descricao, unidade_medida, deposito, data_preenchimento, situacao_rpa):
        pass # Logica de negocio removida por seguranca corporativa



    def exclui_linha(linha):
        pass # Logica de negocio removida por seguranca corporativa



    def lanca_sapiens(codigo_produto, descricao_produto, codigo_familia, codigo_ncm, origem_mercadoria, codigo_cst):
        pass # Logica de negocio removida por seguranca corporativa

        

    def consulta_produtos_tabela():
        pass # Logica de negocio removida por seguranca corporativa




if __name__ == "__main__":
    CadastraProdutosSenior.consulta_produtos_tabela()