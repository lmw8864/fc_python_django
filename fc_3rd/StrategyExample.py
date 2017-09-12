import types


class StrategyExample:
    def __init__(self, func=None):
        self.name = "StrategyPattern 0"
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)


def excute_replacement1(self):
    print(self.name + " replacement 1")


def excute_replacement2(self):
    print(self.name + " replacement 2")


if __name__ == "__main__":
    strategy0 = StrategyExample()

    strategy1 = StrategyExample(excute_replacement1)
    strategy1.name = "StrategyExample 1"

    strategy2 = StrategyExample(excute_replacement2)
    strategy2.name = "StrategyExample 2"

    strategy0.execute()
    strategy1.execute()
    strategy2.execute()
