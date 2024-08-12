**기존 대학 커뮤니티 문제점**

1. 커뮤니티 게시판에 질문
2. 다른 익명의 사용자에게 답변이 오기까지 기다려야 함
3. 사용자에게 답변을 받는 형식이라 불확실

→ 이러한 단점을 보완하고자 질문 즉시 정확한 답변을 받을 수 있는 챗봇을 만들기로 결정

---
## 구현 순서
### 1️⃣ 데이터 구축 및 텍스트 전처리
    
- 세 칼럼(의도, 질문, 답변)으로 데이터 구축
      
![data_construction](https://github.com/user-attachments/assets/55d29491-671f-4c16-822d-3dc900dec6f5)
    
- 토크 나이저를 통해 품사별 POS 태깅
    
![POS_tagging](https://github.com/user-attachments/assets/5634c981-36f2-4348-8987-3d7782bc16db)
    
- 불용어 제거 등 텍스트 전처리
    
![text_preprocessing](https://github.com/user-attachments/assets/e51aa3de-f110-4009-a7bd-cc75c42e5922)

---

### 2️⃣ 의도 분류 모델 생성
    
![build_data_by_Intention](https://github.com/user-attachments/assets/2e969193-1338-4e94-b79c-04fa3341fa69)
    
- CNN으로 딥러닝 모델 구현 및 학습
- 의도별 클래스 라벨링 말뭉치 셋 사용

---

### 3️⃣ 문자 유사도 판별 및 임베딩 작업
- 정확한 정보 전달을 위해 유사도 판별 모델로 KR-SBERT 사용
- 질문 데이터 임베딩 후 pt 파일 저장
- 코사인 유사도
    
![embedding](https://github.com/user-attachments/assets/ffb1af74-ab9c-4488-b3a6-2616148eb69e)

---

### 4️⃣ 챗봇 엔진 서버 개발
- TCP 소켓 모듈을 포함하는 챗봇 엔진 서버 개발 (JSON 형태로 요청과 응답을 주고받음)
    
![chatbot_engine_server](https://github.com/user-attachments/assets/1dfd6300-36f5-489c-9095-04849252c087)
    
- 챗봇 엔진 테스트
    
![engine_test](https://github.com/user-attachments/assets/80ca356e-c1fe-4316-9770-1bc59e6324a1)

---

### 5️⃣ 챗봇 API 구축
- 챗봇 엔진 서버와 웹 간의 통신을 위해 Flask 사용하여 REST API 서버 구축

---

### 6️⃣ 웹 사이트 구현
- HTML/CSS/JS 사용
- (질문 가이드, 퀵메뉴, 질문-답변란, 답변시 의도 분류 결과와 유사도 출력)

### 💬 메인 화면

![main_screen](https://github.com/user-attachments/assets/4a429b34-b0db-4c5c-bcf5-da93653cd3fe)

### 💬 질문 시 답변 화면

![result_screen](https://github.com/user-attachments/assets/1c29b086-fa2b-470c-b900-1984c6356f3f)

### 💬 답변 예시

<aside>
1️. 학과 사무실의 번호와 위치를 물어봤을 때의 답변

![normal_result](https://github.com/user-attachments/assets/731e24a5-62e9-4ef4-91e6-e95720fc3ab3)

</aside>

<aside>
2️. 같은 질문을 다양하게 물어보거나, 오타가 났을 때의 답변

![typing_error_result](https://github.com/user-attachments/assets/bd4459ff-d7f1-4876-b19e-c2f5a69826de)

</aside>

<aside>
3️. 공대가 아닌 다른 단과대에 대해 질문했을 때의 답변

![unanswerable_question_result](https://github.com/user-attachments/assets/a6243428-9834-4207-931e-318d9093f04d)

</aside>
