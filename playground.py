#validate string 

username = input("Enter a valid username: ")

if len(username) > 12:
  print("Username rejected")
  
elif not username.find(" ") == -1:
  print("no spaces allowed")

elif not username.isalpha():
  print("has to be letters only")
else: 
  print("welcome")  
   
# if length < 12 and username.isspace() and username.isalpha():
#   print("username rejected")

# else:
#   print("accepted")