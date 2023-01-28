file_path = "02_data-01-test-score.csv"


class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path
        self.scores = []

    def read_file(self):
        with open(self.file_path) as contents:
            for line in contents:
                self.scores.append(line.strip().split(",")) 

        return self.scores

    def merge_list(self):
        avgs = []
        for score in self.scores:
            score = list(map(int, score))  # map()으로 문자열을 정수로 변환
            avgs.append(sum(score) / len(score))  # sum()으로 리스트의 합을 구하고, len()으로 리스트의 길이를 구한다.

        return sorted(avgs, reverse=False)  # sorted()로 리스트를 올림차순으로 정렬한다.


if __name__ == "__main__":

    read_csv = ReadCSV(file_path)
    read_csv.read_file()
    print(read_csv.merge_list())
