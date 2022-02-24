# 튜플을 이용한 디지털 사진 변환 예제

#### 학습 목표 :

- 튜플을 활용하여 디지털 사진을 표현하는 방식을 이해할 수 있다.
- 디지털 사진을 색 반전이나 흑백 모드로 변환할 수 있다.

## 1. 색

- 색은 3개의 값(빨강색, 초록색, 파랑색)을 가진 튜플로 표현된다.
  ```py
  red = (255, 0, 0)
  blue = (0, 0, 255)
  white = (255, 255, 255)
  black = (0, 0, 0)
  yellow = (255, 255, 0)
  purple = (128, 0, 128)
  ```
- 색을 가진 이미지 만들기 예제
  ```py
  from cs1media import *
  img = create_picture(100, 100, purple)      # 100, 100은 w , h
  img.show()
  img.set_pixels(yellow)     # 모든 픽셀들을 바꾸는 함수
  img.show()
  ```

## 2. 색

- 너비 w, 높이 h 픽셀을 가진 디지털 이미지는 h개의 행과 w개의 열을 가진 직사각형 행렬로 표현된다.
  ||||||
  |--|--|--|--|--|
  |0, 0|1, 0|2, 0|3, 0|4, 0|
  |0, 1|1, 1|2, 1|3, 1|4, 1|
  |0, 2|1, 2|2, 2|3, 2|4, 2|
- 이미지의 각 픽셀은 행렬의 x와 y좌표를 이용해서 접근할 수 있다.
- x좌표의 범위는 0부터 w-1까지, y좌표의 범위는 0부터 h-1까지이다.

```py
>>>img.get(250, 188)    #해당 좌표 픽셀의 색값 가져오기
(101, 104, 51)
>>>img.set(250, 188, (255, 0, 0))   #해당 좌표 픽셀의 색값을 바꾸기
```

## 3. 이미지 반전

```py
from cs1media import *

img = load_picture("../photos/geowi.jpg")
w, h = img.size()
for y in range(h):
    for x in range(w):
        r, g, b = img.get(x,y)
        r, g, b = (255 - r, 255 - g, 255- b)        # 색 반전
        img.set(x, y, (r, g, b))
img.show()
```

## 4. 이미지 흑백 변환

```py
from cs1media import *

threshold = 100
white = (255, 255, 255)
black = (0, 0, 0)
img = load_picture(...)
w, h = img.size()
for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)
        v = (r + g + b) // 3        #r,g,b의 평균값
        if v > threshold:
            img.set(x, y, white)
        else:
            img.set(x, y, black)
img.show()
#대신 이러면 완전 검은색, 완전 흰색으로만 변환을 해서, 우리가 아는 흑백으로 나오지는 않는다.
```

## 정리

1. 여러 픽셀들로 구성된 디지털 사진 이해하기
2. 튜플로 구성된 (red, green, blue), 세 가지 픽셀들의 색 이해하기
3. 디지털 사진의 색 반전과 흑백으로 바꾸는 작업 이해하기
