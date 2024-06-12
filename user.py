from config_reader import ini_config
from database import session, Animal


class User:
    def __init__(self) -> None:
        self._question = 0
        self._reply = []
        self._animal = None

    def next(self) -> list[str] | str:
        self._question += 1
        if self._question == 8:
            return self.final()
        return ini_config("text", "question", f"{self._question}")

    def final(self) -> list[str]:
        self._animal = self.find_best_match()
        ms = ini_config("text", "question", "final").replace("name", self._animal.name).replace("info", self._animal.info)
        return [ms, self._animal.photo]

    def find_best_match(self):
        max_matches = -1
        best_match = None
        records = session.query(Animal).all()
        for record in records:
            matches = (
                (record.food == self._reply[0]) +
                (record.time == self._reply[1]) +
                (record.sociality == self._reply[2]) +
                (record.habitat == self._reply[3]) +
                (record.climate == self._reply[4]) +
                (record.games == self._reply[5]) +
                (record.movement == self._reply[6])
            )
            if matches > max_matches:
                max_matches = matches
                best_match = record
        return best_match
    
    @property
    def animal(self) -> str:
        return self._animal.name

    @property
    def question(self) -> int:
        return self._question
    
    @property
    def reply(self) -> list[int]:
        return self._reply
    
    @reply.setter
    def reply(self, num: int) -> None:
        self._reply.append(num)

    def __str__(self) -> str:
        return f"User {self.question} {self.reply}"
    
    def __repr__(self) -> str:
        return f"User {self.question} {self.reply}"