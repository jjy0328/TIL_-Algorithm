# 힙(Heap)

- 완전 이진 트리 자료구조의 일종
- 항상 root node를 제거
- *min heap* : 루트 노드가 가장 작은 값을 가지므로 우선적으로 제거
- *max heap* : 루트 노드가 가장 큰 값을 가지므로 값이 큰 데이터가 우선적으로 제거됨

`import heapq`

## 최소 힙 구성 함수 : Min-Heaptify()

- 부모 노드로 거슬러 올라가며 자신의 값이 더 작은 경우 위치 교체
<img width="673" alt="2" src="https://user-images.githubusercontent.com/99624568/202403361-f33fb229-f26c-4416-8582-1c95dd2d61be.png">


### 원소 삽입
- 새로운 원소가 삽입되었을 때, O(logN)의 시간 복잡도로 힙 성질 유지

<img width="303" alt="3" src="https://user-images.githubusercontent.com/99624568/202403378-849505ef-4857-46a3-9ff8-2f9a1410b949.png">


### 원소 제거
- 새로운 원소가 삽입되었을 때, O(logN)의 시간 복잡도로 힙 성질 유지
- 마지막 노드가 루트 노드의 위치에 오도록 함
- 이후 루트 노드에서부터 하향식으로 Heaptify() 진행

<img width="660" alt="4" src="https://user-images.githubusercontent.com/99624568/202403398-21679953-488d-4cbe-b00d-ff031b72277b.png">

---

## 이진트리란?

<img width="659" alt="10" src="https://user-images.githubusercontent.com/99624568/202403442-0a71d89b-4974-4d0a-88cb-49a99ef246de.png">


- 컴퓨터 안에서 데이터를 표현할 때 데이터를 각 노드에 담은 뒤 노드를 두 개씩 이어 붙이는 구조
- 이진 트리 : 모든 노드의 자식 노드가 2개 이하인 트리 구조
- 트리 : 가지를 뻗어나가는 것처럼 데이터가 서로 연결되어있음

### 완전 이진 트리

- 데이터가 루트 노드부터 시작해서 자식 노드가 왼쪽 자식노드, 오른쪽 자식 노드로 차근차근 들어가는 구조의 이진 트리
- 중간에 비어있지 않고 완전히 빽빽하게 차있음
- 왼쪽부터 데이터를 채움


---


refer : 동빈나님 이코테 강의
- https://www.youtube.com/watch?v=iyl9bfp_8ag
- https://www.youtube.com/watch?v=AjFlp951nz0
