import random

class User:
    def __init__(self, user_number:int):
        self.number = user_number 

class Resource:
    def __init__(self, resource_number:int):
        self.number = resource_number


class TSOperatingSystem:
    def __init__(self):
        self.user_list = []
        self.resource_list = []

    def generate_users_rand(self):
        randint_users = random.randint(1,30)
        for i in range(randint_users):
            self.user_list.append(User(i))

    def generate_res_rand(self):
        randint_res = random.randint(1,30)
        for i in range(ranidnt_res):
            self.resource_list.append(Resource(i))

    def generate_rand_user_res(self):
        self.generate_res_rand()
        self.generate_users_rand()

    

