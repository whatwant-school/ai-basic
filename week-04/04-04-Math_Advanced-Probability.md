# 4주차 - 기초 튼튼, 수학 튼튼

# 확률론 맛보기 (Mathmatics for Artificial Intelligence)

## Why 확률론

- 회귀분석: 손실함수($L_2$-노름) = 예측 오차의 분산 최소화
- 분류: 교차엔트로피(cross-entropy) = 모델 예측의 불확실성 최소화


## Notation

- 데이터 공간 = $\mathcal{X} \times \mathcal{Y}$
- 데이터 분포 = $\mathcal{D}$
- 데이터 = 확률변수 $(\mathbf{x}, \space \mathbf{y}) \sim \mathcal{D}$
  - $(\mathbf{x}, \space \mathbf{y}) \in \mathcal{X} \times \mathcal{Y}$
- 결합분포 = $P (\mathbf{x}, \space \mathbf{y})$


## 확률변수
확률분포 $\mathcal{D}$에 따라 2가지로 구분 (이산형 / 연속형) ← 데이터 공간이 아니라 분포에 의해 결정


### 이산형 (discrete)

- 확률변수가 가질 수 있는 경우의 수를 모두 고려하여 확률을 더해서 모델링

$$
\mathbb{P} (\mathbf{X} \in \mathbf{A}) = \sum_{\mathbf{x} \in \mathbf{A}} \mathbf{P} ( \mathbf{X} = \mathbf{x})
$$

- $\mathbf{P} ( \mathbf{X} = \mathbf{x})$ : 확률변수가 $\mathbf{x}$ 값을 가질 확률


### 연속형 (continuous)

- 데이터 공간에 정의된 확률변수의 밀도(density) 위에서의 적분을 통해 모델링

$$
\mathbb{P} (\mathbf{X} \in \mathbf{A}) = \int_{\mathbf{A}} \mathbf{P} ( \mathbf{x} )\, dx \\
\space \\
\mathbf{P} ( \mathbf{x} ) = \lim_{h \to 0} {\mathbb{P}( \mathbf{x} - h \le \mathbf{X} \le \mathbf{x} + h ) \over 2h}
$$


## 확률분포

- $P (\mathbf{x})$ : 입력 $\mathbf{x}$에 대한 주변확률분포. $\mathbf{y}$에 대한 정보는 없음

$$
P (\mathbf{x}) = \sum_{\mathbf{y}} \mathbf{P} ( \mathbf{x},\ \mathbf{y} ) \\
\space \\
P (\mathbf{x}) = \int_{\mathbf{y}} \mathbf{P} ( \mathbf{x},\ \mathbf{y} )\, dy
$$

- $P (\mathbf{x}\ \vert\ \mathbf{y})$ : 조건부확률분포. 데이터 공간에서 입력 $\mathbf{x}$와 출력 $\mathbf{y}$ 사이의 관계를 모델링

- 조건부확률 $P (\mathbf{y}\ \vert\ \mathbf{x})$ = 입력변수 $\mathbf{x}$에 대해 정답이 $\mathbf{y}$ 일 확률
  - 연속확률분포의 경우 $P (\mathbf{y}\ \vert\ \mathbf{x})$는 확률이 아니고, 밀도로 해석


## 조건부확률

- 분류문제에서의 $\text{softmax} (\mathbf{W} \phi\ +\ \mathbf{b})$
  - 데이터 $\mathbf{x}$로부터 추출된 특징패턴 $\phi (\mathbf{x})$와 가중치행렬 $\mathbf{W}$을 통해 `조건부확률` $P (\mathbf{y}\ \vert\ \mathbf{x})$를 계산
  - = $P (\mathbf{y}\ \vert\ \phi (\mathbf{x}))$

- 회귀 문제의 경우 `조건부 기대값` $\mathbb{E} \left[ \mathbf{y}\ \vert\ \mathbf{x} \right]$ 추정
  - $\mathbb{E}_{\mathbf{y} \sim P (\mathbf{y}\ \vert\ \mathbf{x})} \left[ \mathbf{y}\ \vert\ \mathbf{x} \right] = \int_{\mathbf{y}} \mathbf{y} \mathbf{P} ( \mathbf{y}\ \vert\ \mathbf{x} )\, dy$


### 통계적 범함수 (statistical functional)

- 확률분포가 주어지면 데이터를 분석하는데 사용 가능한 여러 종류의 통계적 범함수 계산 가능


### 기대값 (expectation)

- 데이터를 대표하는 통계량
- 확률분포를 통해 다른 통계적 범함수를 계산하는데 사용
- 연속확률분포의 경우에는 `적분`, 이산확률분포의 경우에는 `급수`

$$
\begin{matrix}
\mathbb{E}_{\mathbf{x} \sim P (\mathbf{x})} \left[ f (\mathbf{x}) \right] &=& \int_{\mathcal{X}} f(\mathbf{x}) \mathbf{P} (\mathbf{x})\, dx \\
\space \\
\mathbb{E}_{\mathbf{x} \sim P (\mathbf{x})} \left[ f (\mathbf{x}) \right] &=& \sum\limits_{\mathbf{x} \in \mathcal{X}} f(\mathbf{x}) \mathbf{P} (\mathbf{x})
\end{matrix}
$$


## 몬테카를로 샘플링 (Monte Carlo Sampling)

- 확률분포를 모를 때, 데이터를 이용하여 기대값을 계산하기 위해 `몬테카를로 샘플링` 방법 사용
  - 몬테카를로는 이산형/연속형 모두 성립
- 몬테카를로 샘플링은 독립추출만 보정된다면, `대수의 법칙(law of large number)`에 의해 수렴성을 보장

$$
\mathbb{E}_{\mathbf{x} \sim P(\mathbf{x})} \left[ f (\mathbf{x}) \right] \approx {1 \over N}\ \sum\limits_{i = 1}^N f(\mathbf{x}^{(i)}), \quad x^{(i)}\ \overset{i.i.d.}{\sim}\ P(\mathbf{x})
$$
