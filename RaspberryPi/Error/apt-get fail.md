# apt-get error

### Cause
static ip assignment   
정적 IP 할당

### Log
/etc/network/interfaces를 수정하여 고정 IP 할당 시 apt-get update, apt-get upgrade 등의 명령어 실행 실패

### How to solve
/etc/resolv.conf에서 nameserver 8.8.8.8을 입력하여 구글 DNS 서버로 설정