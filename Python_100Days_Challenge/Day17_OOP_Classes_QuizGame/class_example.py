class UserInstagram:
    # Pascal Case is used for classes
    # pass : If you dont want to fill class now

    """
    Constructor
    Initializing an object
    To set variables , counters, switches ...
    __init__ is called each time when you create object
    """

    def __init__(self, user_id, user_name, user_country):
        """Initialise attributes"""
        print("new user being created")
        self.id = user_id
        self.name = user_name
        self.country = user_country

        # default followers
        self.followers = 0
        self.following = 0

    def follow(self, user):
        """self: when this method is called it knows the object that called it"""
        user.followers += 1     # to whom is followed
        self.following += 1     # current object is following


user_1 = UserInstagram("001", "Mehmet", "Finland")
user_2 = UserInstagram("002", "Dr X" , "Sweden")

user_1.follow(user_2)
print(user_2.followers)
print(user_1.following)