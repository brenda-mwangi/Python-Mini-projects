import pywhatkit as kit

with open('names.txt', 'r') as file:
    numbers = [i.strip() for i in file.readlines()]
    print(numbers)

for n in numbers:
    print(n)
# Send a message to a contact on WhatsApp
    kit.sendwhatmsg_instantly(f"{n}", "Good evening!.\nI hope you are doing well. This message is to remind you that we are each contributing 500/= for the *Gratitude Geeks Party*. I have not received your contribution and the deadline, 21st March, is fast approaching. Please send your contribution on time for proper logistics and planning.\n*Brenda Mwangi*,\nClub Treasurer.", 10, True,3)

