#Класс стажер
class Trainee:

    def __init__(self, name: str, surname: str, score: int = 0, passing_grade: int = 10):
        self.name = name
        self.surname = surname
        self.score = score
        self.passing_grade = passing_grade


    @property
    def score(self) -> int:
        return self.__score


    @score.setter
    def score(self, value: int) -> None:
        #Это наверное более правильный вариант, ну мой тоже воркает
        #if not isinstance(value, int) or isinstance(value, bool)
        if type(value) is not int:
            raise ValueError(f"Expected value of type int, got {type(value)}")
        if value < 0:
            raise ValueError("The score shouldn't be less than 0!")
        self.__score = value


    def do_homework(self) -> None:
        """Increases score by 1"""
        self.score = self.score + 1


    def miss_homework(self) -> None:
        """Decreases score by 1"""
        if self.score > 0:
            self.score = self.score - 1


    def visit_lecture(self) -> None:
        """Increases score by 1"""
        self.score = self.score + 1


    def miss_lecture(self) -> None:
        """Decreases score by 1"""
        if self.score > 0:
            self.score = self.score - 1


    def is_passing(self) -> bool:
        """Passage check"""
        return self.score >= self.passing_grade

