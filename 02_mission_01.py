class Score():
    def __init__(self, mid, final):
        self.__mid = mid
        self.__final = final

    @property  # property 데코레이터를 사용하여 mid, final을 읽기 전용으로 만들어준다.
    def mid(self):
        return self.__mid

    @property
    def final(self):
        return self.__final


if __name__ == "__main__":

    score = Score(50, 75)
    print((score.mid + score.final) / 2)
