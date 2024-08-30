#An email splitter program that splits an email into username and domain name

email = input("Enter your email: ")

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(email)
print(f"Your username is {username}")
print(f"Your domain is {domain}")