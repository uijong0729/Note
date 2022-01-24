1. ### Object-Oriented Programming
   
   - Object : 물체, 개체 (객체는 주체의 반의어이므로 오역)
   - 자바가 OOP에 관해서 더 엄격
   
2. ### C++ OOP
   
   - 클래스
   - 개체
   - 생성자
   - 함수 오버로딩
   - 힙에 개체 생성하기
   - 스택에 개체 생성하기
   - ##### 복사 생성자 : 자기 자신을 인수로 받는 메서드. 자기자신을 복사해서 반환 함.
   - 소멸자 
   - 연산자 오버로딩
   
3. ### 누군가가 OOP를 복잡하게 만들었다 (단, 유용한 것도 있음)
   
   - 개채지향 분석과 디자인 (OOAD)
   - 디자인 패턴
   
4. ### 스택
   
   - 예약된 로컬메모리 공간. 일반적으로 1MB 이하
   - 함수 호출과 반환이 이 메모리에서 일어남
   - 스택에 할당된 메모리는 범위를 벗어나면 사라짐
   - 단순히 스택 포인터를 옮김
   - 메모리를 할당 및 해제할 필요가 없음
   - 변수와 매개변수를 위해 필요한 크기는 컴파일 도중에 알 수 있음
   - 스택에 큰 개체를 많이 넣으면 스택오버플로우가 발생할 수 있음
   
5. ### 힙
   
   - 전역 메모리 공간. OS가 지원하는 무수한 메모리 공간.
   - 비어있고 연속된 메모리 블록을 찾아야함
   - 프로그래머가 **직접 할당 및 해제**해야 함
   
6. ### Java가 멤버변수를 초기화하는 방법유추

   ```c
   // Vector의 멤버변수는 모두 int형을 가정
   Vector a = new Vector();
   // Vector크기만큼의 메모리 할당
   void* ptr = malloc(sizeof(Vector));
   // Vector크기만큼의 영역을 0으로 메모리 셋(카피)
   // 모든 비트패턴이 0이면? → 0(정수), 0.0(부동소수점), null로 판단 함
   memset(ptr, 0, sizeof(Vector));
   // 멤버변수 0으로 전부 초기화된 Vector의 포인터를 반환 (new Vector())
   a = (Vector*)ptr;
   ```

7. ### new/delete와 malloc(), free()의 차이는 무엇일까

   - malloc(), free()

     ```yml
     - 라이브러리 함수
     - 헤더파일 필요
     - 쓰임/상황에 따라 오버로딩 가능
     ```

   - new, delete

     ```yml
     - 언어가 제공하는 연산자
     - 별도의 헤더파일 불필요
     - new 연산자로 객체를 할당할 때 생성자가 자동으로 호출된다. 생성자가 생성과 동시에 객체를 초기화 시키는 것으로, 반드시 초기화 되어야하는 기존 타입과 동등한 자격을 가질 수 있게된다.
     ```

   - 할당과 해제는 섞어쓸 수 없다. new로 할당한 메모리는 delete로 해제해야하고 malloc()으로 할당한 메모리는 free로 해제해야한다.

8. ### 기본 생성자

   - 자동적으로 만들어진 생성자는 멤버변수를 초기화 하지 않음

   - 하지만 **모든** **포함된 개체의 생성자를 호출** (개체 속 개체)

   - 컴파일러가 하는 일

     ```yml
     - 생성자가 없으면 기본 생성자 생성
     - 생성자가 있으면 생성자 생성 X
     ```

9. ### 생성자 오버로딩

   - 여러 개의 같은 이름을 가진 생성자
   - 인자의 개수나 자료형은 다름 (매개변수 목록이 일치하는 생성자 호출)

10. ### 소멸자 (C++에만 있음) : Destructor

    - 객체가 지워질 때 호출

    - 메모리 관리를 스스로 해야하기 때문에 

    - 기본 소멸자

      ```c++
      ~ClassName();
      ```

11. ### 구조체 vs 클래스

    1. ###### 기본 접근권한

       - struct : public
       - class : private

    2. ###### C++에서는 구조체에 함수, 생성자 등 클래스에서 할 수 있는거 다 할 수 있는데 무슨 차이일까

       - 어셈블러 : 컴퓨터는 구조체와 클래스를 구분하지 못함. 차이없이 작동함

       - 컴파일러 : 구조체와 클래스를 구분함. 접근권한 문제가 있기 때문

       - C++에서는 구조체를 클래스처럼 쓸 수 있지만, 구조체는 c스타일로만 쓰자

       - 코딩표준 : struct는 순수하게 **데이터** 뿐이어야 함 (Plain Old Data, POD)

         ```
         - 메모리 카피가 용이한 구조로 쓰자 (각 멤버변수는 주소정보가 없는 모두 기본형)
         - 생성자, 소멸자 쓰지말자
         - 함수 X
         - 멤버변수 전부 public
         ```

12. #### 암시적 복사 생성자

    1. 코드에 복사 생성자가 없는 경우 컴파일러가 암시적 복사 생성자를 자동 생성
    2. 암시적 복사 생성자는 얕은 복사(shallow copy)를 수행
       - 멤버 별 복사
       - 각 멤버의 값을 복사
       - 개체인 멤버변수는 **그 개체의 복사 생성자가 호출**됨
       - 포인터는 얕은 복사 : 주소만 복사되기 때문에 두 개체가 데이터를 공유하는 상황이 발생

    3. 클래스 안의 멤버변수에 포인터가 포함되어 있다면 프로그래머가 직접 깊은 복사(deep copy)를 수행하는 복사 생성자를 만들어줘야 한다.

13. #### friend 키워드

    - 클래스 정의 안에 friend 키워드를 사용가능

    - 다른 클래스나 함수가 나의 private 또는 protected 멤버에 접근할 수 있게 허용

    - friend 클래스

      ```c++
      class X
      {
          // friend 클래스
      	friend class Y;
      private:
      	int mPrivateInt;
      }
      /////////////////////////////////////////////////////////////////////////////////
      class Y
      {
      public:
          void Y::Foo(X& x)
          {
              // 바로 접근
              x.mPrivateInt += 10;
          }
      }
      ```

    - friend 함수

      ```c++
      // X.h
      class X
      {
          // friend 함수
      	friend void Foo(X& x);
      private:
      	int mPrivateInt;
      }
      
      // GlobalFunc.cpp
      // friend 함수를 다른 cpp에서 정의
      void Foo(X& x)
      {
      	x.mPrivateInt += 10;
      }
      ```

    - 연산자 오버로딩에 필요한 friend 함수

      - friend함수는 멤버 함수가 아님
      - 하지만 다른 클래스의 private 멤버에 접근할 수 있음

    

    

    