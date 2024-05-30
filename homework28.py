# # Ստեղծեք Car class, որը ներկայացնում է մեքենա, որը կարելի է կայանել ավտոկայանատեղիում:
# # Car class-ը ստեղծման ժամանակ պետք է տրամադրվի car_id ատրիբուտով: Բոլոր հետագա գործողությունները պետք է հաշվի առնեն car_id-ն։

# # Ստեղծեք ParkingLot class, որը կառավարում է մեքենաների կայանումը: 
# # Այս class-ը մի քանի գործառույթներ ունի. այն պետք է օգնի կայանել մեքենան, բաց թողնել մեքենան և հաղորդել ազատ մնացած տեղերի քանակը:
# # ParkingLot class-ը պետք է ունենա հետևյալ ատրիբուտները և մեթոդները.
# #      total_spots ատրիբուտ - ավտոկայանատեղիում կայանատեղերի ընդհանուր թիվը, որը պետք է տրամադրվի կայանատեղիի օբյեկտի ստեղծման ժամանակ,
# #      park(car) մեթոդ - կայանում է մեքենան (Car) ավտոկայանատեղիում, 
# #      Եթե ավտոկայանատեղին ամբողջությամբ զբաղված է, այն պետք է տպի՝ Parking lot is full։
# #      release(car) մեթոդ - ավտոմեքենան (Car) բաց է թողնում ավտոկայանատեղից։ 
# #           Եթե մեքենան կայանատեղիում չէ, պետք է տպի` Car not found in the parking lot,
# #           Եթե մեքենան կայանատեղիում է, պետք է հարցնի մեքենայի վարորդից input-ի միջոցով թե քանի ժամ է մեքենան գտնվել ավտոկայանատեղիում, 
# #           և գանձի համապատասխան վճարը (1 ժամ - 500 դրամ)։
# #      spots_left() մեթոդ - վերադարձնում է կայանատեղիում առկա կայանման տեղերի քանակը
# #      cash_register() մեթոդ - վերադարձնում է գանձված վճարների գումարը կայանված ավտոմեքենաներից



# class Car:
#     def __init__(self, car_id):
#         self.car_id = car_id

# class ParkingLot:
#     def __init__(self, total_spots):
#         self.total_spots = total_spots
#         self.parked_cars = {}

    
#     def park(self, car):
#         self.car = car
#         if len(self.parked_cars) < self.total_spots:
#             self.parked_cars[car.car_id] = 1
#         else:
#             print("Parking lot is full.")
        

#     def release(self, car):
#         if car.car_id in self.parked_cars:
#             hours = int(input("Enter the number of hours =  "))
#             fee = hours *500
#             print(car_id, fee)
#         else:
#            print("Car not found in the parking")

#     def spots_left(self):
#         return self.total_spots - len(self.parked_cars)



# parking_lot = ParkingLot(10)
# car1 = Car("ABC123")
# parking_lot.park(car1)
# parking_lot.release(car1)
# print(parking_lot.spots_left())
















class BankUser:
    def __init__(self, name, surname, age, card, money, password):
        if (self._is_valid_name(name) and self._is_valid_name(surname) and self._is_valid_age(age)
                and self._is_valid_card(card) and self._is_valid_money(money) and self._is_valid_password(password)):
            self._name = name
            self._surname = surname
            self._age = age
            self.__card = card
            self.__money = money
            self.__password = password
            self.__login_tries = 0
            self.account_blocked = False

        else:
            raise ValueError('Incorrect parameters.')

    @staticmethod
    def _is_valid_name(name):
        return isinstance(name, str) and name.isalpha()

    @staticmethod
    def _is_valid_age(age):
        return isinstance(age, int) and age > 0

    @staticmethod
    def _is_valid_card(card):
        return isinstance(card, str) and (len(card) == 16 and card.isdigit()
                                          or len(card) == 19 and card[4::5] == '   ' and card.replace(' ', '', 3).isdigit())

    @staticmethod
    def _is_valid_money(money):
        return isinstance(money, int|float) and money >= 0

    @staticmethod
    def _is_valid_password(password):
        return isinstance(password, str) and len(password) >= 8

    def user_info(self):
        print(f"{self._name} {self._surname}, {self._age} years old")

    def _is_correct_password(self):
        if self.account_blocked:
            print("Your account is blocked")
            return False

        if self.__password == input('Enter your password: '):
            return True
        else:
            self.__login_tries += 1
            if self.__login_tries >= 3:
                 self.account_blocked = True
            else:
                print('Incorrect password.')
            return False

    def account_info(self):
        if self._is_correct_password():
            print(f'{self.__card}, ${self.__money}')

    def add_money(self, x):
        if self._is_correct_password():
            if self._is_valid_money(x):
                self.__money += x
                print(f'${self.__money}')
            else:
                raise ValueError('Incorrect parameter.')

    def sub_money(self, x):
        if self._is_correct_password():
            if self._is_valid_money(x):
                if self.__money >= x:
                    self.__money -= x
                    print(f'${self.__money}')
                else:
                    print('Not enough money.')
            else:
                raise ValueError('Incorrect parameter.')


u1 = BankUser("Valentina", 'Chakhoyan', 26, "1234 5678 9102 3456", 100000, '12345678')
u1.user_info()
