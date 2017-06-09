import mail_send
import getpass
import mail_list

sender = input("Type your email: ")
password = getpass.getpass("Type your password: ")
print("Do you want to send an email to how many people?")
print("1 - One")
print("2 - Many")
response = int(input())
if response == 1:
    receiver = input("Type the receiver's email: ")
    mail = input("Type the file name: ")
    print("Sending mail to",receiver,"...",end="")
    mail_send.sendMail(sender,password,receiver,mail)
    print("OK")
else:
    fileName = input("Type the email list file's name: ")
    emailFile = input("Type the email file name: ")
    mail_list.sendToMailsInList(fileName,sender, password,emailFile)
