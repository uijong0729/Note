1. ##### 새로운 기능이 매우 많지만 대부분 사용되지 않음

   - C++의 진짜 전문가는 사용하지 말아야 할 기능을 아는 사람

2. ##### bool 데이터형

   - old style : 0(거짓)이거나 0이 아닌 값(참)
   - new style : false, true

3. ##### 참조(Reference)

   - 포인터를 사용하는 좀 더 안전한 방법

   - 참조에 의한 호출 구현

     ```c
     void swap(int* arg1, int* arg2) {
     	int tmp = *arg1;
     	*arg1 = *arg2;
     	*arg2 = tmp;
     }
     
     int main() {
     	int num1 = 10;
     	int num2 = 20;
     	swap(&num1, &num2);
     	// 결과 : num1 == 20, num1 == 10
     }
     ```

   - C/C++는 포인터가 없으면 모든 타입에 대해 똑같이 값에 의한 호출로 동작한다. (값 복사)

     ```c
     struct Human {
     	int age;
     	int height;
     }
     
     void Increase(Human human) {
     	human.age = human.age + 1;
     }
     
     int main() {
     	Human human;
     	human.age = 10;
     	Increase(human);
     	// 결과 : human.age == 10 그대로
     }
     ```

   - 포인터 연산 주의점
   
     ```c
     void Increase(Human* arg) {
     	// Human이 4바이트 int형 2개를 가진 구조체이므로
         // Human의 사이즈 만큼(8byte) 증가한다. (배열과 유사)
     	arg = arg + 1;
     }
     ```
   
   - 포인터와 참조는 같은 어셈블리 명령어를 생성한다. 
   
   - 참조의 장점
   
     ```c
     // 포인터로도 만들 수 있지만 참조를 이용한 스왑함수도 가능
     // 이것이 더 안전하기 때문에 권장됨
     // 1. number1, number2는 NULL을 대입할 수 없음 (구조적으로 NULL이 오지않는다)
     // 2. 우리가 소유하지 않은 메모리 장소를 가리킬 수 없음
     void Swap(int& number1, int& number2) {
     	int tmp = number1;
     	number1 = number2;
     	number2 = tmp;
     }
     ```
   
     

