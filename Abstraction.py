





from abc import ABC, abstractmethod
class Basketball(ABC):
    def Points(self, amount):
        print("Your points amount in the first quarter: ",amount)

    @abstractmethod
    def total_points(self, amount):
        pass

class Scoring(Basketball):
    def total_points(self, amount):
        print('Your total points after the game were {}!'.format(amount))

obj = Scoring()
obj.Points("10")
obj.total_points("50")
