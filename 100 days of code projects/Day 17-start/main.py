class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(1,"Brenda")    
user2 = User(2, "Brian")
print(user2.followers) 
print(user_1.following)

user_1.follow(user2)
print(user2.followers)
print(user_1.following)
