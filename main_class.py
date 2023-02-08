class User:
    def __init__(self, userid, username):
        self.id = userid
        self.username = username
        self.followers = 0


user_1 = User("001", "angela")

print(user_1.id)
print(user_1.username)
print(user_1.followers)
