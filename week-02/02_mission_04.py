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
        sums = []
        for score in self.scores:
            sum = 0
            for i in range(len(score)):
                sum += int(score[i])
            sums.append(sum)

        return sums


if __name__ == "__main__":

    read_csv = ReadCSV(file_path)
    print(read_csv.read_file())
    print(read_csv.merge_list())
