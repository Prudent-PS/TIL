# 프로그램에서 사용하는 객체와 객체의 형태

#### 0. 학습 목표 :

- 객채(objects)와 형태(types)를 이해할 수 있다.
- 변수(variables)를 이해할 수 있다.

## 1. 객체

- Python 프로그램에서 사용하는 각각의 데이터는 **객체(Object)**라 부릅니다.
- 객체의 크기는 작을 수도 있고(숫자 3), 매우 클 수도 있다(사진 파일).
- 모든 객체는 형태(Type)을 가지고 있다.

## 2. 객체 생성

### 간단한 객체:

- 숫자 : 숫자 그대로 적는다
  ```py
  13
  3.141592
  -5
  3 + 6j
  ```
- 문자열 : 문자열을 따옴표(",') 사이에 적는다.
  ```py
  "CS101 is good"
  'CS101 is wonderful'
  ```
  > 주의 : 둘다 동일한 용도로 사용할 수 있지만, 혼용해서는 사용하면 안된다.

### 복잡한 객체

1. 복잡한 객체는 함수를 부르는 방법으로 만든다.
   ```py
   from cs1robots import *
   Robot()         #로봇 객체를 만드는 함수 호출
   ```
2. 사진을 불러 객체로 보관
   ```py
   from cs1media import *
   load_picture("photos/geowi.jpg")
   ```
3. 튜플을 사용한 객체 생성

- 튜플(Tuple)은 다른 객체들을 포함하는 객체.
- 여러 객체를 "grouping"해서 하나의 객체로 가지도록 하는 것
  ```py
  (3, 2.5, 7)
  ("red", "yellow", "green")
  (29199991, "Hong Gildong")  #튜플이 포함하는 객체의 type이 달라도 무관
  ```

## 3. 형태

- 모든 객체는 형태(Type)을 가지고 있다.
- 객체의 형태는 객체가 할 수 있는 일과, 객체를 이용해 할 수 있는 일을 결정한다.
- Python에서는 "type명령어"을 이용해서 객체가 어떤 형태를 가지고 있는지 알 수 있다.
  ```py
  >>> type(3)
  <class 'int'>
  >>> type(True)
  <class 'bool'>
  >>> type(Robot())
  <class 'cslrobots.Robot>
  >>> type((3, -1.5, 7))
  <class 'tuple'>
  >>> type(load_picture("geowi.jpg"))
  <class 'cs1media.Picture'>
  ```
  > 주의 : 복잡한 객체들의 형태는 함수.(class 이름)으로 type이 명시된다.

## 4. 이름

- 객체에는 이름을 줄 수 있다.
  ```py
  message = "CS101 is fantastic"
  n = 17
  img = load_picture("goewi.jpg")
  ```

## 5. 이름 규칙

- 영어 문자, 숫자, 그리고 밑줄 문자(\_)로만 이루어져야 한다.
- 숫자는 이름의 첫 글자로 올 수 없다.
- 파이썬에서 등록된 키워드(예약어)와 동일한 이름은 지을 수 없다.
  - ex) `def`, `if`, `else`, `while`
- 이름은 대소문자를 구분한다.
  - ex) `Pi`와 `pi`는 다른 이름이다.

### 6. 변수

- 이름과 **변수(Variable)**는 같은 의미
- 변수에 대입된 객체는 변수의 **값**이라 부른다.
- `None`이라는 이름의 특별한 객체는 **비었다**는 것을 의미하기 위해 사용된다.
  ```py
  n = None
  >>> type(n)
  <class 'NoneType'>
  ```

## 7. 멤버 변수

- 객체는 멤버 함수(Method)를 통해 여러가지 행위를 할 수 있다.
- 멤버 함수는 **점(.) 연산자**를 통해 실행 가능

  ```py
  >>> hubo = Robot()
  >>> hubo.move()         #멤버 함수사용1
  >>> hubo.turn_left()    #2

  >>> img = load_picture("geowi.jpg")
  >>> print(img.size())   #3
  (58, 50)
  >>> img.show()          #4

  >>> b = "banana"
  >>> print(b.upper())    #5, 해당 문자열의 소문자들을 모두 대문자로 바꾸는 메소드
  BANANA
  ```

## 7. 객체의 특징

- 하나의 객체는 여러 이름을 가질 수 있다.
- 이름이 가리키는 객체는 바뀔 수 있다.

  ```py
  hubo = Robot("yellow")
  hubo.move()
  ami = hubo
  ami.turn_left()
  hubo.move           #ami와 hubo가 가리키는 객체가 같고, 모든 동작은 "yellow"라는 찐 객체가 실행함

  hubo = Robot("blue")
  hubo.move()         #"blue"가 움직임
  ami.move()          #"yellow"가 움직임, 이름이 가리키는 객체가 바뀜
  ```

## 정리

객체와 형태 그리고 변수에 대한 이해를 할 수 있었다.
