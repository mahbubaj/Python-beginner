import random

name = "Mahbuba"
# question = "Should I cry after every ML lecture?"
question = ""
answer = ""
if question == "":
  print("Type a valid question")
else:
  print("Magic 8-Ball's answer:")
  print(name + " asks: " + question)
random_number = random.randint(1,9)
# print(random_number)
if random_number == 1:
  print("{answer}".format(answer="Yes - definitely"))
elif random_number == 2:
  print("{answer}".format(answer="It is decidedly so"))
elif random_number == 3:
  print("{answer}".format(answer="Without a doubt"))
elif random_number == 4:
  print("{answer}".format(answer="Reply hazy, try again"))
elif random_number == 5:
  print("{answer}".format(answer="Ask again later"))
elif random_number == 6:
  print("{answer}".format(answer="Better not tell you now"))
elif random_number == 7:
  print("{answer}".format(answer="My sources say no"))
elif random_number == 8:
  print("{answer}".format(answer="Outlook not so good"))
elif random_number == 9:
  print("{answer}".format(answer="Very doubtful"))
else:
  print("Error")

