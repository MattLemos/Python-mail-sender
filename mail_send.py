import smtplib

def sendMail(sender, password, receiver, file_name):
    #setup
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()

    myList = []#lista que recebe o conteudo do email
    nome = file_name #nome do arquivo
    fp = open(nome,'r')
    myList.append(fp.read()) #adiciona o conteudo do arquivo na lista
    fp.close()

    conteudo = ''.join(myList) #conteudo da mensagem
    myLogin = sender #email do remetente
    myPass = password #senha do remetente
    destino = receiver #email do destinatario

    mail.starttls() #inicia o processo de envio
    mail.login(myLogin,myPass) #login na conta que envia
    mail.sendmail(myLogin,destino,conteudo) #envia o email
    mail.close(); #fecha o processo de email
