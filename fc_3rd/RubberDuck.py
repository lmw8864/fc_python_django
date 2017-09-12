from Duck import Duck


class RubberDuck(Duck):
    def display(self):
        print("Rubber Duck 입니다")

    def quack(self):
        print("뀍뀍")

if __name__ == "__main__":
    duck = RubberDuck()
    duck.display()
    duck.quack()
