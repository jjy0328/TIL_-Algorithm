# 더하기 혹은 곱하기

0과 1이 포함된 연산은 더하기, 그 외의 숫자들은 모두 곱하기로 처리합니다. 숫자들의 리스트를 deque로 만든 후, 순서대로 숫자를 하나씩 pop합니다. 숫자가 남아있을 때까지 다음을 반복합니다. 이전 혹은 현재 숫자가 0 또는 1이면 이전 숫자와 현재 숫자를 더한 값을 이전 숫자로 설정합니다. 그 외는 이전 숫자와 현재 숫자를 곱한 값을 이전 숫자로 설정합니다. 반복이 끝난 후 이전 숫자를 반환합니다.

# 문제 조건
- 입력 : 첫째 줄에 여러 개의 숫자로 구성도니 하나의 문자열 S가 주어집니다. (1<=S의 길이<=20)
- 출력 : 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.