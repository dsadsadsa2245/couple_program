# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.
import time


class InsufficientPhoneCharge(Exception):
    pass


class InvalidError(Exception):
    pass


class Phone:
    charge = 100

    def check_data(self):
        self.charge = self.charge - 0.5
        if self.charge < 0:
            self.charge = self.charge + 0.5
            return f"Недостаточно заряда для данной операции!"
        return f"Вы проверили заряд.Ваш заряд {self.charge} %"

    def listen_music(self):
        self.charge = self.charge - 5
        if self.charge < 0:
            self.charge = self.charge + 5
            return f"Недостаточно заряда для данной операции!"
        return f"Вы послушали музыку.Ваш заряд {self.charge} % "

    def watch_video(self):
        self.charge = self.charge - 7
        if self.charge < 10:
            self.charge = self.charge + 7
            return f"Недостаточно заряда для данной операции!"
        return f"Вы посмотрели видео.Ваш заряд {self.charge} %"

    def charge_phone(self):
        while self.charge < 100:
            self.charge = self.charge + 1
            print(f" Ваш заряд :{self.charge} %")
            time.sleep(0.0000000000000000000001)

    def __init__(self):

        while self.charge > 0:
            a = input(
                "Вы можете выполнить три действия: проверить зарядку (check_data), послушать музыку (listen_music), посмотреть видео (watch_video): ")

            try:
                if a == "check_data":
                    print(self.check_data())
                elif a == "listen_music":
                    print(self.listen_music())
                elif a == "watch_video":
                    print(self.watch_video())
                elif a == "charge_phone" and self.charge <100:
                    self.charge_phone()
                else:
                    raise InvalidError("Вы ввели неправильные данные!")
            except InvalidError as e:
                print("Ошибка:", e)
                continue
        b = input("Внимание заряд вашего телефона очень низкий.Некомендкем начать зарядку.Введите charge_phone")
        if b == "charge_phone":
            self.charge_phone()
            self.__init__()


obj1 = Phone()
