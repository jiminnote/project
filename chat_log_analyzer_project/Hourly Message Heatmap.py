from collections import Counter, defaultdict
import re
import matplotlib.pyplot as plt
import platform
from project.chat_log_analyzer_project.chat_log_analyzer import user_message_count

hour_counter = defaultdict(Counter)

with open('KakaoTalkChats.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if re.match(r'^\d{4}년 \d+월 \d+일', line) and ',' in line:
            try:
                # 날짜와 시간 파싱
                time_part, msg_part = line.split(',', 1)  # ✅ 콤마 기준으로 1번만 나누기  # 예: '2023년 4월 8일 오전 10:21'
                user, _ = msg_part.split(':', 1)
                user = user.strip()
                match = re.search(r'(오전|오후) (\d+):(\d+)', time_part)
                if match:
                    meridiem, hour, minute = match.groups()
                    hour = int(hour)
                    if meridiem == '오후' and hour != 12:
                        hour += 12
                    elif meridiem == '오전' and hour == 12:
                        hour = 0  # 12AM → 0시

                    hour_counter[user][hour] += 1
            except Exception:
                continue

# ✅ 한글 폰트 설정
if platform.system() == 'Darwin':  # macOS
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:  # Linux
    plt.rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 📊 그래프 그리기
hours = list(range(24))
# counts = [hour_counter[h] for h in hours]

colors = ['gold','skyblue','lightgreen','violet']
for idx, (user, counter) in enumerate(hour_counter.items()):
    counts = [counter[h] for h in hours]
    plt.bar(hours, counts, alpha=0.7, label=user, color=colors[idx%len(colors)])

# plt.bar(hours, counts)

plt.xticks(hours)
plt.xlabel("시간 (시)")
plt.ylabel("메시지 수")
plt.title("시간대별 메시지 빈도")
plt.grid(True)
plt.legend()


# 📌 메시지 수 요약 텍스트를 그래프에 추가
sorted_users = sorted(user_message_count.items(), key=lambda x: x[1], reverse=True)
summary_lines = [f"{user}: {count}" for user, count in sorted_users]
summary_text = " > 참여도 순위 \n" + "\n".join(summary_lines)

# 그래프 오른쪽 상단에 텍스트 삽입
plt.gcf().text(0.75, 0.6, summary_text, fontsize=10, bbox=dict(facecolor='white', alpha=0.6))

plt.show()


