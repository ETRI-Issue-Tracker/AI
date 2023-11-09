# Korean HateSpeech Dataset

<a href="https://github.com/kocohub/korean-hate-speech">데이터셋 출처</a> </br> <hr>

데이터  셋의 bias, hate column 기준으로 편향성 공경성 컨텐츠를 판단.<br>
<strong>
```
정상적인 컨텐츠 -> 0
공격적 컨텐츠 -> 1
편향적 컨텐츠 -> 2 
공격적 + 편향적 컨텐츠 -> 3
```
</strong>
<img width="402" alt="image" src="https://github.com/ETRI-Issue-Tracker/AI/assets/74136791/e0f5b5d0-90cc-48c3-8aa5-83f7c79a14d2">
<br>
의 경우로 labeling하여 학습

<br>


```
python -m uvicorn main:app --reload --host=[host ip] --port=[port number]
```
위 명령어로 실행
