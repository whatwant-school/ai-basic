# 4주차 - 기초 튼튼, 수학 튼튼

## Pandas 2

- https://github.com/TEAMLAB-Lecture/AI-python-connect/tree/master/codes/ch_3/part-2


### groupby

- SQL에서의 groupby와 같은 개념

```python
# "Team" 기준으로 "Points" 컬럼을 sum()
df.groupby("Team")["Points"].sum()

###
Team
Devils    1536
Kings     2285
Riders    3049
Royals    1505
kings      812
Name: Points, dtype: int64
```

- 2개 이상의 column을 묶을 수도 있음

```python
h_index = df.groupby(["Team", "Year"])["Points"].sum()

###
Team    Year
Devils  2014    863
        2015    673
Kings   2014    741
        2016    756
        2017    788
Riders  2014    876
        2015    789
        2016    694
        2017    690
Royals  2014    701
        2015    804
kings   2015    812
Name: Points, dtype: int64
```


### Hierarchical index

- 2개 column groupby → index가 2개

```python
h_index.index

###
MultiIndex([('Devils', 2014),
            ('Devils', 2015),
            ( 'Kings', 2014),
            ( 'Kings', 2016),
            ( 'Kings', 2017),
            ('Riders', 2014),
            ('Riders', 2015),
            ('Riders', 2016),
            ('Riders', 2017),
            ('Royals', 2014),
            ('Royals', 2015),
            ( 'kings', 2015)],
           names=['Team', 'Year'])
```

- `:`을 이용해서 2개의 index를 사용

```python
h_index["Devils":"Kings"]

###
Team    Year
Devils  2014    863
        2015    673
Kings   2014    741
        2016    756
        2017    788
Name: Points, dtype: int64
```


### Hierarchical index - unstack

- Group으로 묶여진 데이터를 matrix 형태로 전환

```python
h_index.unstack()

###
Year	2014	2015	2016	2017
Team				
Devils	863.0	673.0	NaN	NaN
Kings	741.0	NaN	756.0	788.0
Riders	876.0	789.0	694.0	690.0
Royals	701.0	804.0	NaN	NaN
kings	NaN	812.0	NaN	NaN
```


### Hierarchical index - swaplevel

- index level을 변경

```python
h_index.swaplevel()

###
Year  Team  
2014  Devils    863
2015  Devils    673
2014  Kings     741
2016  Kings     756
2017  Kings     788
2014  Riders    876
2015  Riders    789
2016  Riders    694
2017  Riders    690
2014  Royals    701
2015  Royals    804
      kings     812
Name: Points, dtype: int64
```

### Hierarchical index - sort_index

- index를 정렬
- 이전에는 `sortlevel()`이었으나, deprecated

```python
# h_index.swaplevel().sortlevel(0)
h_index.swaplevel().sort_index(level=0)

###
Year  Team  
2014  Devils    863
      Kings     741
      Riders    876
      Royals    701
2015  Devils    673
      Riders    789
      Royals    804
      kings     812
2016  Kings     756
      Riders    694
2017  Kings     788
      Riders    690
Name: Points, dtype: int64
```


### Hierarchical index - operation

- 최근에는 `groupby()`를 명시적으로 선언토록 함

```python
# h_index.sum(level=0)
h_index.groupby(level=0).sum()

###
Team
Devils    1536
Kings     2285
Riders    3049
Royals    1505
kings      812
Name: Points, dtype: int64
```


### groupby - grouped

- groupby에 의해 split된 상태 추출

```python
grouped = df.groupby("Team")

for name,group in grouped:
    print (name)
    print (group)

###
Devils
     Team  Rank  Year  Points
2  Devils     2  2014     863
3  Devils     3  2015     673
Kings
    Team  Rank  Year  Points
4  Kings     3  2014     741
6  Kings     1  2016     756
7  Kings     1  2017     788
Riders
      Team  Rank  Year  Points
0   Riders     1  2014     876
1   Riders     2  2015     789
8   Riders     2  2016     694
11  Riders     2  2017     690
Royals
      Team  Rank  Year  Points
9   Royals     4  2014     701
10  Royals     1  2015     804
kings
    Team  Rank  Year  Points
5  kings     4  2015     812
```


### grouped - get_group

- 특정 key값을 가진 그룹의 정보 추출

```python
grouped.get_group("Riders")

###

Team	Rank	Year	Points
0	Riders	1	2014	876
1	Riders	2	2015	789
8	Riders	2	2016	694
11	Riders	2	2017	690
```


### grouped - Aggregation

- 요약된 통계 정보를 추출

```python
grouped.agg(sum)

###

Rank	Year	Points
Team			
Devils	5	4029	1536
Kings	5	6047	2285
Riders	7	8062	3049
Royals	5	4029	1505
kings	4	2015	812
```

- 여러가지를 섞은 report를 뽑아낼 수도 있음

```python
grouped['Points'].agg([np.sum, np.mean, np.std])

###

sum	mean	std
Team			
Devils	1536	768.000000	134.350288
Kings	2285	761.666667	24.006943
Riders	3049	762.250000	88.567771
Royals	1505	752.500000	72.831998
kings	812	812.000000	NaN
```


### grouped - Transformation

- 개별 데이터 변환

```python
# 원본 데이터 살펴보면,
grouped = df.groupby("Team")

for name,group in grouped:
    print (name)
    print (group)

###
Devils
     Team  Rank  Year  Points
2  Devils     2  2014     863
3  Devils     3  2015     673
Kings
    Team  Rank  Year  Points
4  Kings     3  2014     741
6  Kings     1  2016     756
7  Kings     1  2017     788
Riders
      Team  Rank  Year  Points
0   Riders     1  2014     876
1   Riders     2  2015     789
8   Riders     2  2016     694
11  Riders     2  2017     690
Royals
      Team  Rank  Year  Points
9   Royals     4  2014     701
10  Royals     1  2015     804
kings
    Team  Rank  Year  Points
5  kings     4  2015     812
```

```python
# index 빼고, values에 적용
score = lambda x: (x - x.mean()) / x.std()
grouped.transform(score)

###
Rank	Year	Points
0	-1.500000	-1.161895	1.284327
1	0.500000	-0.387298	0.302029
2	-0.707107	-0.707107	0.707107
3	0.707107	0.707107	-0.707107
4	1.154701	-1.091089	-0.860862
5	NaN	NaN	NaN
6	-0.577350	0.218218	-0.236043
7	-0.577350	0.872872	1.096905
8	0.500000	0.387298	-0.770596
9	0.707107	-0.707107	-0.707107
10	-0.707107	0.707107	0.707107
11	0.500000	1.161895	-0.815759
```

- min / max 같은 Series 데이터에 적용될 때에는 key값으로 grouped된 데이터 기준

```python
# index 순서대로 정렬
score = lambda x: (x.max())
grouped.transform(score)

###
Rank	Year	Points
0	2	2017	876
1	2	2017	876
2	3	2015	863
3	3	2015	863
4	3	2017	788
5	4	2015	812
6	3	2017	788
7	3	2017	788
8	2	2017	876
9	4	2015	804
10	4	2015	804
11	2	2017	876
```


### grouped - Filteration

- 특정 조건으로 데이터 검색

```python
df.groupby('Team').filter(lambda x: len(x) >= 3)

###
Team	Rank	Year	Points
0	Riders	1	2014	876
1	Riders	2	2015	789
4	Kings	3	2014	741
6	Kings	1	2016	756
7	Kings	1	2017	788
8	Riders	2	2016	694
11	Riders	2	2017	690
```


### pivot_table

- 엑셀에서의 피봇테이블

```python
# 원본 데이터 확인
df_phone.head()

###
index	date	duration	item	month	network	network_type
0	0	2014-10-15 06:58:00	34.429	data	2014-11	data	data
1	1	2014-10-15 06:58:00	13.000	call	2014-11	Vodafone	mobile
2	2	2014-10-15 14:46:00	23.000	call	2014-11	Meteor	mobile
3	3	2014-10-15 14:48:00	4.000	call	2014-11	Tesco	mobile
4	4	2014-10-15 17:27:00	4.000	call	2014-11	Tesco	mobile
```

```python
df_phone.pivot_table(["duration"],
                     index=[df_phone.month,df_phone.item], 
                     columns=df_phone.network, aggfunc="sum", fill_value=0)

###
# 표가 깨져서 여기에 표현하기 어려움
```

### crosstab

- 2개 column에서 교차 빈도, 비율, 덧셈 등을 구할 때 사용
- Pivitg table의 특수한 형태
- User-Item Rating Matrix 등을 만들 때 사용 가능

```python
# 원본 데이터 확인
df_movie.head()

###
critic	title	rating
0	Jack Matthews	Lady in the Water	3.0
1	Jack Matthews	Snakes on a Plane	4.0
2	Jack Matthews	You Me and Dupree	3.5
3	Jack Matthews	Superman Returns	5.0
4	Jack Matthews	The Night Listener	3.0
```

```python
pd.crosstab(index=df_movie.critic,
            columns=df_movie.title,
            values=df_movie.rating,
            aggfunc="first").fillna(0)

###
title	Just My Luck	Lady in the Water	Snakes on a Plane	Superman Returns	The Night Listener	You Me and Dupree
critic						
Claudia Puig	3.0	0.0	3.5	4.0	4.5	2.5
Gene Seymour	1.5	3.0	3.5	5.0	3.0	3.5
Jack Matthews	0.0	3.0	4.0	5.0	3.0	3.5
Lisa Rose	3.0	2.5	3.5	3.5	3.0	2.5
Mick LaSalle	2.0	3.0	4.0	3.0	3.0	2.0
Toby	0.0	0.0	4.5	4.0	0.0	1.0
```


### merge

- 2개의 데이터를 하나로 합침

```python
# 원본 데이터 확인 - df_a
raw_data = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_score': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'test_score'])
df_a

###
subject_id	test_score
0	1	51
1	2	15
2	3	15
3	4	61
4	5	16
5	7	14
6	8	15
7	9	1
8	10	61
9	11	16
```

```python
# 원본 데이터 확인 - df_b
raw_data = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
df_b

###
subject_id	first_name	last_name
0	4	Billy	Bonder
1	5	Brian	Black
2	6	Bran	Balwner
3	7	Bryce	Brice
4	8	Betty	Btisan
```

- `on` = inner join

```python
# 동일한 subject_id 값을 갖고 있는 데이터만 추출
pd.merge(df_a, df_b, on='subject_id')

# column 명이 다를 경우에는 아래와 같은 방식으로 표현할 수도 있음
# pd.merge(df_a, df_b, left_on='subject_id', right_on='subject_id')

###
subject_id	test_score	first_name	last_name
0	4	61	Billy	Bonder
1	5	16	Brian	Black
2	7	14	Bryce	Brice
3	8	15	Betty	Btisan
```