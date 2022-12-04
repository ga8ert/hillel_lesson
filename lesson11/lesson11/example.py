# OOP

# main principles

# abstraction
# encapsulation
# inheritance
# polymorphism


# class User:
#     pass
#
#
# user1 = User()
#
# print(type(user1))
# print(isinstance(user1, User))

#
# class User:
#     name = None
#     age = 30
#
#     def say_hello(self):
#         res = f'Hello, my name is {self.name} i\'m {self.age} old'
#         return res
#
#
# user1 = User()
#
# user1.name = 'Bill'
#
# print(user1.name)
# print(user1.age)
#
# print(user1.say_hello())  # say_hello(user1)
# # print(user1.say_hello())  # User.say_hello(user1)
#
# user2 = User()
# user2.name = 'Bob'
# print(user2.say_hello())  # User.say_hello(user2)
# # print(User.say_hello(user2))
#

# class User:
#     name = None
#     age = 30
#
#     def say_hello(self, prefix='Hello'):
#         res = f'{prefix}, my name is {self.name} i\'m {self.age} old'
#         return res
#
#
# user1 = User()
#
# user1.name = 'Bill'
#
# print(user1.say_hello())
# print(user1.say_hello('Hi!'))


# class User:
#     name = None  # class variables
#     age = 30
#
#     def say_hello(self, prefix='Hello'):
#         res = f'{prefix}, my name is {self.name} i\'m {self.age} old'
#         return res
#
#
# user1 = User()
#
# user1.name = 'Bill'
#
# print(user1.say_hello())
# print(user1.say_hello('Hi!'))
#
# print(User.name)
# print(User.age)

#
# class Myclass:
#     lst = [1, 3]
#
#     def change_lst(self, data):
#         self.lst.append(data)
#
#
# obj1 = Myclass()
#
# obj1.change_lst('e')
#
# print(obj1.lst)
# print(Myclass.lst)


# class User:
#     name = 'Bill'
#     age = 30
#
#     def say_hello(self, prefix='Hello'):
#         res = f'{prefix}, my name is {self.name} i\'m {self.age} old'
#         return res
#
#
# user1 = User()
#
# # user1.name = 'Joe'
# print(user1.name)
#
# User.name = 'Tom'
#
# print(user1.name)


# class User:
#     name = 'Bill'
#     age = 30
#
#     def say_hello(self, prefix='Hello'):
#         res = f'{prefix}, my name is {self.name} i\'m {self.age} old'
#         return res
#
#
# user1 = User()
#
# attrname = 'name'
#
# # print(user1.attrname)
#
# res = getattr(user1, 'age2', None)
#
# print(res)
#
# setattr(user1, 'age', 20)
#
# print(user1.age)
#
# res = hasattr(user1, 'age')
# print(res)
#
# user1.new_attr = '234567u'
#
# print(user1.new_attr)
#
# setattr(user1, 'age1234', 20)
#
# print(user1.age1234)


# class User:
#     # public
#     name = 'Bill'
#     age = 30
#
#     # protected
#     _phone = '+380631231223'
#
#     # private
#     __address = 'jhgfdbiruhv bygfvi kj v'
#
#     def say_hello(self, prefix='Hello'):
#         res = self.__say_hello(prefix)
#         return res
#
#     def __say_hello(self, prefix='Hello'):
#         res = f'{prefix}, my name is {self.name} i\'m {self.age} old. ' \
#               f'Phone number {self._phone}. Address {self.__address}.'
#         return res
#
#
# user1 = User()
# print(user1.name)
# print(user1._phone)
# print(user1.say_hello())
# print(user1.__say_hello())
#
# # print(user1.__address)
# print(user1._User__address)


# class Human(object):
#     name = 'Bill'
#     age = 30
#
#     def say_hello(self):
#         res = f'Hi, my name is {self.name} i\'m {self.age} old. '
#         return res
#
#
# human1 = Human()
# print(dir(human1))
#
#
# class User(Human):
#     login = 'khbcivef'
#     pwd = 'aesrfgt'
#
#     def say_hello(self):
#         res = f'Hi, my name is {self.name} i\'m {self.age} old. Login {self.login}'
#         return res
#
#
# user1 = User()
# # print(dir(user1))
# print(human1.say_hello())
# print(user1.say_hello())
#
#
# print(isinstance(human1, Human))
# print(isinstance(human1, User))
# print(isinstance(user1, Human))
# print(isinstance(user1, User))


class Human:
    name = None
    age = None

    def __init__(self, new_name, new_age):
        # print(f'Inside init {self.name} {self.age}')
        self.name = new_name
        self.age = new_age

    def say_hello(self):
        res = f'Hi, my name is {self.name} i\'m {self.age} old. '
        return res

    def change_name(self, name):
        # validation here
        self.name = name


human1 = Human(new_name='Tom', new_age=20)
human2 = Human(new_name='Joe', new_age=30)

print(human1.say_hello())
print(human2.say_hello())
print(human2.change_name('Tamara'))
