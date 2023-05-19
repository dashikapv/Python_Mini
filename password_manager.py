pwd = input("What is the master password: ")

def view():
  with open('Passwords.txt','r') as f:
    for line in f.readlines():
      print(line)
  


def add():
  name = input("Account name: ")
  password = input("Password: ")

  with open('Passwords.txt','a')as f:
    f.write(name + " " + password + "\n")

while True:
  mode = input("Would you like to add new password or view existing ones(view,add),press q to quit? ").lower()

  if mode =='q':
    break

  if mode == "view":
    view()
  elif mode == "add":
    add()
  else:
    print("Invalid mode")
