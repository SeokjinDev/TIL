# MySQL the specified port already in use
## 개요
MySQL 설치 시 Type and Networking 페이지에서 포트에 느낌표 발생   
이전 버전으로 인한 오류로써 삭제하면 해결된다.

## 해결방법
1. 리소스 모니터 열기   
2. port number 3306 찾기   
3. 포트 번호가 3306인 프로세스의 PID 기억하기   
4. CMD를 관리자 권한으로 실행하여 아래 명령어 입력하기
    ```CMD
    taskkill /F /PID xxxx
    ```
