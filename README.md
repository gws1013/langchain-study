# langchain-study
랭체인 및 관련하여 공부를 했던 내용을 정리한 Repository 입니다.

0. langchain 설치
!pip install -U langchain
!pip install -U langchain-openai
- pip 보다 설치 속도가 빠른 uv를 사용하는 것도 좋아보임 

2. openai platform api를 활용하는 간단한 방법.
- os.environ['OPENAI_API_KEY'] = string, ex) "sk-proj-"
  - 초기 비용 5달러 (구매 필수)
  - 키 노출 절대 금지
  - 키 운용과 관련하여 로컬 .env 또는 Secret manager (비밀번호 관리 툴 사용)
    - AWS SM은 비용이 비쌈, Bitwarden이 현실적으로 가능한 스토리 https://bitwarden.com/
- model: string, ex) "gpt-5.2", "gpt-4o" 등 (모델명을 의미)
- input: string, ex) "ai agent가 뭔가요?" 등 (프롬프트 문구를 의미)

2. langchain 기초편
- langchain.chat_models 내 init_chat_model.py 의 init_chat_model 함수
  - model
    - 복잡한 작업 모델이면 comp_model = init_chat_model("gpt-5.4")
    - 간단한 작업 모델이면 easy_model = init_chat_model("gpt-4o-mini")
    - 하지만, 가장 중요한건 목적에 맞는 모델 선택이 중요! (모델마다 어떤 장점과 단점이 있는지 알고있으면 좋을듯)
  - temperature (창의성)
    - 무작위성을 결정
    - 0~1.0 값을 가짐, 높을수록 창의적, 낮을수록 논리적 (보통 0.6 정도로 사용)
  - maxtoken
    - 응답의 최대 길이를 제한
    - 비용관리 및 출력 토큰 통제
  - timeout
    - 응답 대기시간 제한 시스템 무한 대기 방지
  - max_retries
    - 네트워크 오류 발생 시 자동 재시도를 통해 연결 성공률 확보

4. 
5. 
