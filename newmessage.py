import pywhatkit as kit

with open('names.txt', 'r') as file:
    numbers = [i.strip() for i in file.readlines()]
    print(numbers)
for n in numbers:
    print(n)
# Send a message to a contact on WhatsApp
    kit.sendwhatmsg_instantly(f"{n}", "Good morning!.\n I have not received your 500/=  contribution for the *Gratitude Geeks Party* contribution. Today is the only day left. Please send your contribution on time for proper logistics and planning. \nM-pesa number: 0740730056\nM-pesa name: Charles Gitau\n\nYours, *Brenda Mwangi*,\nClub Treasurer.", 45, True,15)

