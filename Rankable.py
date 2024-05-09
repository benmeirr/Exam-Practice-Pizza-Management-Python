from abc import ABC, abstractmethod


class Rankable(ABC):

    @abstractmethod
    def calculate_rank(self):
        pass

    @abstractmethod
    def calculate_ranged_rank(self, rank_range):
        pass
