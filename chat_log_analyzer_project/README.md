# 📝 KakaoTalk Chat Log Analyzer

카카오톡 대화 파일을 분석하여 유저별 메시지 수, 단어 빈도, 시간대별 활동량 등을 시각화하는 Python 기반 미니 프로젝트입니다.

---

## 🔎 개발 히스토리
- 2025.07.12: 프로젝트 최초 구현 완료
- 2025.07.13: pandas 기반 통계 분석 + 시각화 기능 리팩토링
  - `datetime` 파싱 오류 수정 (오전/오후 → AM/PM)
  - `.to_pickle()`로 데이터 저장 및 재사용

## 📌 주요 기능

- **유저별 메시지 수** 집계 및 정렬 출력
- **유저별 자주 사용하는 단어 Top 5**
- **전체 대화에서 가장 많이 등장한 단어 Top 10**
- **‘보고싶다’, ‘배고파’ 등 키워드 사용 횟수**
- **시간대별 메시지 빈도 바 차트** + 유저별 활동 비교
- **그래프 내 텍스트 요약 포함 (대화 참여도 순위)**

---

## 🛠 사용 방법

### 1. 카카오톡 채팅 파일 준비
- **카카오톡 대화 내보내기** → `텍스트만` 저장
- 파일명을 `KakaoTalkChats.txt` 로 변경하고 루트 폴더에 넣어주세요.

### 2. 분석 실행

```bash
python3 chat_log_analyzer.py
```
그래프 기반 시각화를 보고 싶다면 `Hourly Message Heatmap.py` 파일을 실행하세요.

### 🔒 .gitignore 설정

개인 대화 파일은 공개되지 않도록 `.gitignore`에 `KakaoTalkChats.txt`를 추가했습니다. 🙂





