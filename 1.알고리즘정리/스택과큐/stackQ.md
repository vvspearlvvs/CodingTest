### 스택

먼저 들어온 데이터가 나중에 나가는 선입후출 자료구조

입구와 출구가 동일한 '박스를 쌓는 형태

구현방법 : 리스트 자료형을 이용 

stack=[] 

삽입 : stack.append()

삭제 : stack.pop()

<h3>큐</h3>

먼저 들어온 데이터가 먼저 나가는 선입선출 자료구조

입구와 출구가 모두 떨려있는 '터널을 통과하는 형태'

구현방법 : dequqe 라이브러리 사용 (**from collections import deque**)

queue=deque() 

삽입 : queue.append() 

삭제 : queue.popleft()

pop()을 하게 되면 원소를 꺼낸 뒤에 원소의 위치를 조정해야해서 시간이 더오래걸림

<h3>우선순위큐(힙)</h3>

가장 우선순위가 높은 데이터가 먼저 나가는 선입선출 자료구조

단순히 N개의 데이터를 우선순위 큐에 넣었다가 모두 꺼내는 작업은 정렬과 동일(O(NlogN))

힙특징 : 완전이진트리 자료구조로, 항상 루트노드를 제거한다. 

최소힙 : 루트노드가 가장 작은 값을 가짐 ->작은데이터 우선적으로 제거 , 넣고 꺼내면 오름차순 정렬

최대힙 : 루트노드가 가장 큰 값을 가짐 -> 큰 데이터 우선적으로 제거, 넣고 꺼내면 내림차순 정렬

*완전이진트리

루트노드부터 시작하여 왼쪽자식노드, 오른쪽자식노드 순서대로 데이터가 차례대로 삽입되는 트리

*최소힙 구성함수 : Min-Heapify()

부모노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우 위치 교체 

구현방법 : heap 라이브러리 사용 ( import heap)

heapsort(arr):

h=[]

result=[]

for value in arr: #모든 원소를 차례대로 힙에 삽입

​	heap.heappush(h,value)

for i in range(len(h)): #힙에 삽입한 모든 원소를 차례대로 꺼내오기 

​	result.append(heap.heappop(h))

삽입 O(logN) 예시: 2 삽입

<img src="C:\Users\gg664\AppData\Roaming\Typora\typora-user-images\image-20210708001011082.png" alt="image-20210708001011082" style="zoom:50%;" />

제거 O(logN) 예시 : 2삭제

가장 마지막 노드가 루트노드의 위치에 오도록 한다.

이후 루트노드에서 하향식으로(더 작은 자식노드로) Heapify()진행 

<img src="C:\Users\gg664\AppData\Roaming\Typora\typora-user-images\image-20210708001225155.png" alt="image-20210708001225155" style="zoom:50%;" />

<img src="C:\Users\gg664\AppData\Roaming\Typora\typora-user-images\image-20210708001250512.png" alt="image-20210708001250512" style="zoom:50%;" />