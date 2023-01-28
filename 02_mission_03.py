file_path = "02_data-01-test-score.csv"


def read_file(file_path):

    scores = []
    with open(file_path) as contents:
        # csv 파일에 header가 없으므로 바로 데이터를 읽어온다.
        for line in contents:
            scores.append(line.strip().split(","))  # strip()으로 공백 및 줄바꿈 제거, split()으로 쉼표로 구분

    return scores


if __name__ == "__main__":

    print(read_file(file_path))
