import mail_send

def sendToMailsInList(file_name, sender, password,emailFile):
    name = file_name
    mail_list = open(name,"r")
    for line in mail_list:
        receiver = line
        print("Sending mail to",line)
        mail_send.sendMail(sender, password,receiver,emailFile)
        print("OK")
    mail_list.close()
