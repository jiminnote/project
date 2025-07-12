import re
from collections import defaultdict, Counter

# 준비 :  유저별로 데이터를 정리하기 위한 딕셔너리 구조를 만듬
user_words = defaultdict(list)
user_message_count = defaultdict(int)
all_words = []

# 메시지 줄 추출
with (open('KakaoTalkChats.txt', 'r', encoding='utf-8') as f):
    for line in f:
        line = line.strip()
        if re.match(r'^\d{4}년 \d+월 \d+일', line) and ',' in line:
            if not any(keyword in line for keyword in ['이모티콘', 'https:', '사진']):
            # 예: 2023년 4월 8일 오전 10:21, 지민 : 안녕하세요
                try:
                    time_part, msg_part = line.split(',', 1)
                    user, message = msg_part.split(':', 1)
                    user = user.strip()
                    message = message.strip()
                    words = message.split()
                    user_words[user].extend(words)
                    user_message_count[user] += 1
                except ValueError:
                    continue  # 혹시 예외적인 줄 건너뛰기
# 유저별 메시지 수
print("📈 메시지 수 (많은 순):")
for user, count in sorted(user_message_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{user}: {count}")



# 유저별 단어 Top5
print("\n🔤 유저별 단어 Top5:")
for user, words in user_words.items():
    print(f"\n👤 {user}")
    for word, freq in Counter(words).most_common(5):
        print(f"  {word}: {freq}")

# 전체 채팅 단어 Top 10
for words in user_words.values():
    all_words.extend(words)

word_count = Counter(all_words)

print("\n 📊 전체 채팅 단어 Top 10:")
for word, count in word_count.most_common(10):
    print(f"{word}: {count}")

print("\n📊 유저별 '보고싶다' 단어 사용 횟수:")
for user, words in user_words.items():
    count = sum(1 for word in words if '보고싶다' in word)
    print(f"{user}: {count}회")

# 이렇게하면 miss you 의 보고싶다가 아니라 해보고싶다 가보고싶다 도 들어감..개선 해야함

## 개선안
print("\n📊 유저별 진짜 '보고싶다'고 한 횟수:")
for user, words in user_words.items():
    count = sum(1 for word in words if word.startswith('보고싶다'))
    print(f"{user}: {count}회")

print("\n📊 유저별 '배고파' 단어 사용 횟수:")
for user, words in user_words.items():
    count = sum(1 for word in words if '배고파' in word)
    print(f"{user}: {count}회")

