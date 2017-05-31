import mail_send
import getpass

sender = input("Type your email: ")
password = getpass.getpass("Type your password: ")
receiver = input("Type the receiver's email: ")
mail = input("Type the file name: ")

print("Sending mail to",receiver,"...",end="")
mail_send.sendMail(sender,password,receiver,mail)
print("OK")
