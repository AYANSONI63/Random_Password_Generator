import random
import string 

pass_len = 12

charValues = string.digits + string.punctuation + string.ascii_letters
# list comprehension [function for i in range(n)]

password = "".join([random.choice(charValues) for i in range(pass_len)])
# Above used function is an complex function

# for i in range(pass_len):  # This approach is normal approach 

#     password += random.choice(charValue)


print("Your random password is :",password)
