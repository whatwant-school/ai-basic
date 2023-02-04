import csv

if __name__ == '__main__':
    seoung_nam_data = []
    header = []
    rownum = 0

    with open("02_korea_floating_population_data.csv", "r", encoding="cp949") as p_file:
        csv_data = csv.reader(p_file)

        for row in csv_data:
            if rownum == 0:
                header = row

            # “행정구역”필드 데이터 추출, 한글 처리로 유니코드 데이터를 cp949로 변환
            location = row[7]

            if location.find(u"성남시") != -1:
                seoung_nam_data.append(row)
            rownum += 1

    with open("02_seoung_nam_floating_population_data.csv", "w", encoding="utf8") as s_p_file:
        writer = csv.writer(s_p_file, delimiter='\t', quotechar="'", quoting=csv.QUOTE_ALL)
        writer.writerow(header)

        for row in seoung_nam_data:
            writer.writerow(row)
