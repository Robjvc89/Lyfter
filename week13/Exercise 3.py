from datetime import datetime

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth  
    
    @property
    def age(self):
        today = datetime.today()
        birth_date = datetime.strptime(self.date_of_birth, '%Y-%m-%d')
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age


def check_adult(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError("User is underage. Access to adult content is only allowed for users 18 or older.")
        return func(user, *args, **kwargs)
    return wrapper


@check_adult
def view_adult_content(user):
    print("Access granted to adult content!")


user1 = User("2000-06-15")  # 25 years old today
user2 = User("2010-06-15")  # 15 years old today


view_adult_content(user1)


view_adult_content(user2)  # This will raise a ValueError
