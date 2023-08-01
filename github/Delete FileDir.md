# Github에서 파일/디렉토리 삭제하기
## Description
레포지토리에서 원하는 디렉토리나 파일을 명령어로 삭제하는 방법

## Commands
* Local & Remote   
    ```
    $ git rm {File name/Dir Name}
    $ git commit -m "message"
    $ git push
    ```
* Remote Only
    ```
    $ git rm --cached -r {File name/Dir Name}
    $ git commit -m "message"
    $ git push
    ```