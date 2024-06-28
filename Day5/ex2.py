age = int(input("How old are you? "))

if age < 16:
      print("You are eligible for the child rate of 80p.")
elif age >= 60:
      print("You are eligible for the OAP rate of £1.")
else:
      print("You must pay the standard rate of £1.50.")
