from task1.trainee import Trainee


class HardworkingTrainee(Trainee):

    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score = self.score + 2

#