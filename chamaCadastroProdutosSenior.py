import sys

from cadastraProdutosSenior import CadastraProdutosSenior
from enviaEmailItensCadastrados import EnviaEmailItensCadastrados

sys.path.append(r"C:\rpa\Python")

from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer




try:
    CadastraProdutosSenior.consulta_produtos_tabela()
except Exception as e:
    destinatarios_email = []
    destinatarios_email.append("nicolas.nasario@COMPANY_NAME.com.br")
    destinatarios_email.append("israel.martins@COMPANY_NAME.com.br")
    destinatarios_email.append("davi.lopes@COMPANY_NAME.com.br")
    
    assunto = "Erro no RPA de Cadastro de Produtos Senior"

    mensagem = f"""
    <html>
    <body>
        <p>Ocorreu um erro durante a execução do RPA de Cadastro de Produtos Senior:<br><br>
        <strong>{str(e)}</strong></p>
        
        <br><br>
        <p>Atenciosamente,<br>
        Equipe de RPA COMPANY_NAME</p>
    </body>
    </html>
    """

    zimbra = ZimbraMailer()
    zimbra.envia_email(destinatarios_email=destinatarios_email, assunto_email=assunto, mensagem_email=mensagem)


try:
    tabela = EnviaEmailItensCadastrados.consulta_tabela_itens_cadastrados()
except Exception as e:
    destinatarios_email = []
    destinatarios_email.append("nicolas.nasario@COMPANY_NAME.com.br")
    destinatarios_email.append("israel.martins@COMPANY_NAME.com.br")
    destinatarios_email.append("davi.lopes@COMPANY_NAME.com.br")

    assunto = "Erro no RPA de Envio de Email Itens Cadastrados"

    mensagem = f"""
    <html>
    <body>
        <p>Ocorreu um erro durante a execução do RPA de Envio de Email Itens Cadastrados:<br><br>
        <strong>{str(e)}</strong></p>
        
        <br><br>
        <p>Atenciosamente,<br>
        Equipe de RPA COMPANY_NAME</p>
    </body>
    </html>
    """

    zimbra = ZimbraMailer()
    zimbra.envia_email(destinatarios_email=destinatarios_email, assunto_email=assunto, mensagem_email=mensagem)


try:
    EnviaEmailItensCadastrados.envia_email_itens_cadastrados(tabela)
except Exception as e:
    destinatarios_email = []
    destinatarios_email.append("nicolas.nasario@COMPANY_NAME.com.br")
    destinatarios_email.append("israel.martins@COMPANY_NAME.com.br")
    destinatarios_email.append("davi.lopes@COMPANY_NAME.com.br")

    assunto = "Erro no RPA de Envio de Email Itens Cadastrados"

    mensagem = f"""
    <html>
    <body>
        <p>Ocorreu um erro durante a execução do RPA de Envio de Email Itens Cadastrados:<br><br>
        <strong>{str(e)}</strong></p>
        
        <br><br>
        <p>Atenciosamente,<br>
        Equipe de RPA COMPANY_NAME</p>
    </body>
    </html>
    """

    zimbra = ZimbraMailer()
    zimbra.envia_email(destinatarios_email=destinatarios_email, assunto_email=assunto, mensagem_email=mensagem)