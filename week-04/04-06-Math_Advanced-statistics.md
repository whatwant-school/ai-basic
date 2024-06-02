# 4주차 - 기초 튼튼, 수학 튼튼

# 통계학 맛보기 (Statistics)

## 통계적 모델링

- 적절한 가정 위에서 확률분포를 추정(inference)
- 유한한 데이터 관찰로 모집단의 정확한 분포 파악 불가능 → 근사적으로 확률분포 추정


### 모수적(parametric) 방법론

- 데이터가 특정 확률분포를 따른다고 선험적으로(a priori) 가정한 후 그 분포를 결정하는 모수(parameter)를 추정


### 비모수(nonparametric) 방법론

- 특정 확률분포를 가정하지 않고 데이터에 따라 모델의 구조 및 모수의 개수가 유연하게 변경


## 확률분포 - 예제

데이터에 따라서 확률분포를 가정할 수 있지만, 기계적으로 하면 안되고 데이터를 생성하는 원리를 먼저 고려하는 것이 원칙

- 2개의 값(0 또는 1) → 베르누이 분포
- n개의 이산적인 값 → 카테고리 분포
- [0, 1] 사이의 값 → 베타 분포
- 0 이상의 값 → 감마 분포, 로그 정규 분포 等
- $\mathbb{R}$ 전체 → 정규 분포, 라플라스 분포 等


## 모수 (parameter)

### Notation

- 평균 : $\mu$
- 분산 : $\sigma^2$


### 정규분포의 모수 추정

- 표본평균

$$
\bar{X} = {1 \over N}\ \sum_{i = 1}^{N} X_i
\quad\
\mathbb{E} \left[ \bar{X} \right] = \mu
$$

- 표본분산
  - $N$이 아니고 $N - 1$로 나누는 이유는 불편(unbiased) 추정량을 구하기 위함

$$
S^2 = {1 \over {N - 1}}\ \sum_{i = 1}^{N} (X_i\ -\ \bar{X})^2
\quad\
\mathbb{E} \left[ S^2 \right] = \sigma^2
$$


###  표집분포 (sampling distribution)
- 통계량의 확률분포
- 중심극한정리(Central Limit Theorem)
  - 표본평균의 표집분포는 $N$이 커질수록 정규분포 $N(\mu,\ {\sigma^2 \over N})$를 따른다
  - 모집단의 분포가 정규분포를 따르지 않아도 성립


## 최대가능도 추정법 (maximum likelihood estimation, MLE)
이론적으로 가장 가능성이 높은 모수를 추정하는 방법 중 하나

$$
\hat{\theta}_{MLE} = \underset{\theta}{\text{argmax}}\ L (\theta\ ;\ \mathbf{x}) = \underset{\theta}{\text{argmax}}\ P (\mathbf{x}\ \vert\ \theta)
$$

- 가능도(likelihood) 함수는 모수 $\theta$를 따르는 분포가 $\mathbf{x}$를 관찰할 가능성을 뜻하지만, 확률로 해석하면 안된다

- 데이터 집합 $\mathbf{X}$가 독립적으로 추출되었을 경우 로그가능도를 최적화
  - 데이터가 독립일 경우, 로그를 사용하면 가능도의 곱셈을 로그가능도의 덧셈으로 변환 가능
  - 경사하강법으로 가능도 최적화 시 미분 연산 사용 → 로그가능도를 사용하면 연산량이 $O(n^2)$에서 $O(n)$으로 감소
  - 대부분 손실함수의 경우 경사하강법을 사용하므로, `음의 로그가능도(negative log-likelihood)`를 최적화

$$
L (\theta\ ;\ \mathbf{X}) = \prod_{i=1}^n P (\mathbf{x}_i\ \vert\ \theta)
\quad \Rightarrow \quad
\log L (\theta\ ;\ \mathbf{X}) = \sum_{i = 1}^{n} \log P (\mathbf{x}_i\ \vert\ \theta)
$$


### 최대가능도 추정법 예제 : 정규분포

- 정규분포를 따르는 확률변수 $\mathbf{X}$로부터 표본 $\{ x_1,\ ...,\  x_n\}$을 얻었을 때 최대가능도 추정법을 이용하여 모수를 추정하면?

$$
\hat{\theta}_{MLE} = \underset{\theta}{\text{argmax}}\ L (\theta\ ;\ \mathbf{x}) = \underset{\mu,\ \sigma^2}{\text{argmax}}\ P (\mathbf{x}\ \vert\ \mu,\ \sigma^2) \\
\space \\
\log L (\theta\ ;\ \mathbf{X}) = \sum_{i = 1}^{n} \log P (\mathbf{x}_i\ \vert\ \theta) = \sum_{i = 1}^{n} \log {1 \over \sqrt{2 \pi \sigma^2}}\ e^{- {{\left\vert x_i - \mu \right\vert}^2 \over 2 \sigma^2}} \\
\space \\
= - {n \over 2}\ \log 2 \pi \sigma^2\ -\ \sum_{i = 1}^{n} {{\left\vert x_i - \mu \right\vert}^2 \over 2 \sigma^2}
$$

- $\theta = (\mu,\ \sigma)$에 대해 미분

$$
0 = {\partial \log L \over \partial \mu} = - \sum_{i = 1}^{n} {x_i - \mu  \over \sigma^2} \\
\space \\
\quad \Rightarrow \quad
\hat{\mu}_{MLE} = {1 \over n} \sum_{i = 1}^{n} x_i
\space \\
\space \\
0 = {\partial \log L \over \partial \sigma} = - {n \over \sigma} + {1 \over \sigma^3} \sum_{i = 1}^{n} {\left\vert x_i - \mu  \right\vert}^2 \\
\space \\
\quad \Rightarrow \quad
\hat{\sigma}_{MLE}^2 = {1 \over n} \sum_{i = 1}^{n} (x_i - \mu)^2
$$


### 최대가능도 추정법 예제 : 카테고리 분포

- 카테고리 분포 Multinoulli $(\mathbf{x}; p_1,\ ...,\ p_d)$를 따르는 확률변수 $\mathbf{X}$로부터 독립적인 표본 $\{ x_1,\ ...,\  x_n\}$을 얻었을 때 최대가능도 추정법을 이용하여 모수를 추정하면?

$$
\hat{\theta}_{MLE} = \underset{p_1,\ ...,\ p_d}{\text{argmax}}\ \log P(\mathbf{x}_i\ \vert\ \theta) = \underset{p_1,\ ...,\ p_d}{\text{argmax}}\ \log \left( \prod_{i=1}^n\ \prod_{k=1}^d p_k^{x_i,\ k} \right) \\
$$

- 카테고리 분포의 모수는 다음 제약식을 만족해야 한다 : $\sum\limits_{k = 1}^{d} p_k = 1$

$$
\log \left( \prod_{i=1}^n\ \prod_{k=1}^d p_k^{x_i,\ k} \right) = \sum_{k = 1}^{d} \left( \sum_{i = 1}^{n} x_i, k \right)\ \log p_k \\
\space \\
n_k = \sum_{i = 1}^{n} x_i, k
$$

- $n_k$ : 주어진 데이터 $x_i$에 대해서 $k = 1$인 데이터의 개수

$$
\log \left( \prod_{i=1}^n\ \prod_{k=1}^d p_k^{x_i,\ k} \right) = \sum_{k = 1}^{d} n_k\ \log p_k
\quad \text{with} \quad
\sum_{k = 1}^{d} p_k = 1 \\
$$

- 라그랑주 승수법을 통해 최적화 문제를 풀 수 있음

$$
\Rightarrow \quad \mathcal{L} (p_1,\ ...,\ p_k,\ \lambda) = \sum_{k =1}^d n_k\ \log p_k\ +\ \lambda \left(1 - \sum_{k} p_k \right) \\
\space \\
0 = {\partial \mathcal{L} \over \partial p_k} = {n_k \over p_k} - \lambda \\
\space \\
0 = {\partial \mathcal{L} \over \partial \lambda} = 1 - \sum_{k = 1}^{d} p_k \\
\space \\
p_k = {n_k \over \sum\limits_{k=1}^d n_k}
$$


## 딥러닝에서 최대가능도 추정법

- 딥러닝 모델의 가중치를 $\theta = (\mathbf{W}^{(1)},\ ...,\ \mathbf{W}^{(L)})$라 표기했을 때, 분류 문제에서 softmax 벡터는 카테고리 분포의 모수 $(p_1,\ ...,\ p_k)$를 모델링 한다.
- one-hot 벡터로 표현한 정답레이블 $\mathbf{y} = (y_1,\ ...,\ y_k)$을 관찰 데이터로 이용해 확률분포인 softmax 벡터의 로그가능도를 최적화 할 수 있다.

$$
\hat{\theta}_{MLE} = \underset{\theta}{\text{argmax}}\ {1 \over n}\ \sum_{i=1}^{n}\ \sum_{k=1}^{K}y_{i, k}\ \log (\text{MLP}_{\theta} (\mathbf{x}_i)_k)
$$


### 확률분포의 거리(distance)

- 총변동 거리 (Total Variation Distance, TV)
- 쿨백-라이블러 발산 (Kullback-Leibler Divergence, KL)
- 바슈타인 거리 (Wasserstein Distance)


### 쿨백-라이블러 발산 (Kullback-Leibler Divergence, KL)

$$
\mathbb{KL}(P \Vert Q) = \sum_{\mathbf{x} \in \mathcal{X}} P(\mathbf{x})\ \log \left( {P(\mathbf{x}) \over Q(\mathbf{x})} \right) \\
\space \\
\mathbb{KL}(P \Vert Q) = \int_{\mathcal{X}} P(\mathbf{x})\ \log \left( {P(\mathbf{x}) \over Q(\mathbf{x})} \right)  dx
$$

### 쿨백-라이블러 분해

$$
\mathbb{KL}(P \Vert Q) = - \mathbb{E}_{\mathbf{x} \sim P(\mathbf{x})} [\ \log Q(\mathbf{x})\ ] + \mathbb{E}_{\mathbf{x} \sim P(\mathbf{x})} [\ \log P(\mathbf{x})\ ]
$$

- 분류 문제에서 정답레이블을 $P$, 모델 예측을 $Q$라 두면 최대가능도 추정법은 쿨백-라이블러 발산을 최소화 하는 것과 동일