name = "list.txt"
mail_list = open(name,"r")
for line in mail_list:
    line = line.split()
    print(line)
mail_list.close()
