class Duck:
    def __init__(self):
        print("기본 오리 생성")

    def display(self):
        print("기본 오리 입니다.")

    def quack(self):
        print("꽥꽥")

if __name__ == "__main__":
    duck = Duck()
    duck.display()
    duck.quack()
