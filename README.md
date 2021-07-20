# Loguru
해당 프로젝트의 목적은 로깅 loguru의 익히기 위한 목적으로 한다.


## Prerequisitive
```shell
$ PIPENV_VENV_IN_PROJECT=true pipenv install --three
```

```shell
$ pipenv install
```

## Getting Started

### Logging How to work
로깅을 어떻게 동작할까? 아래 그림을 통하여 확인 할 수 있다.

<img src="images/logging-process.jpeg">

- Level: 로깅 정보의 중요도를 나타낸다.
    ```python
    logger.info("info level")
    ```

- Filter: 로깅매칭하는 경우 로깅에 대한 추가
    ```txt
    "password": "1234" ---> "password": "비밀번호처리"
    ```

- Formatting: 어떤 형태로 출력할 것인가?
    ```python
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ```

- Handler: 어디에다가 정보를 출력할 것인가?
    ```python
    # 콘솔, 파일,DB,소켓, 큐 등으로  출력
    file_handler = logging.FileHandler('my.log')
    mylogger.addHandler(file_handler)
    ```

### 사용방법



### 무엇을 로깅할 것인가?


**항목**
- 


## Reference
- [python logging](https://kimeuichan.github.io/posts/python-logging-with-loguru/)
- [loguru](https://loguru.readthedocs.io/en/stable/)
- [loguru for blog](https://kimeuichan.github.io/posts/python-logging-with-loguru/)
- [logging howto](https://docs.python.org/3.7/howto/logging.html)
- [python-logging](https://opensource.com/article/17/9/python-logging)
