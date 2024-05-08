from abc import ABC, abstractmethod


class Surprisable(ABC):
    @abstractmethod
    def activate_surprise(self):
        pass