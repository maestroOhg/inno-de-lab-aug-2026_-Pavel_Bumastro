from task1.trainee import Trainee


class Cohort:

    def __init__(self, title: str, trainees: list[Trainee] | None =  None) -> None:
        self.title = title
        self.trainees = [] if trainees is None else trainees


    def add_trainee(self, trainee: Trainee) -> None:
        """Add trainee to list(group trainees)"""
        self.trainees.append(trainee)


    def conduct_lecture(self) -> None:
        """Conduct lecture(add score to trainees)"""
        for trainee in self.trainees:
            trainee.visit_lecture()


    def get_passing_students(self) -> list[Trainee]:
        """Return list of trainee's passing students(is_passing -> True)"""
        return [trainee for trainee in self.trainees if trainee.is_passing()]

#