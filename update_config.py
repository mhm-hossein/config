import requests
import os

# لیست فایل‌های کانفیگ
configs = [
    "https://raw.githubusercontent.com/mhm-hossein/config/main/list1.txt",
    "https://raw.githubusercontent.com/mhm-hossein/config/main/list2.txt",
    # ادامه فایل‌های کانفیگ
]

# فایل برای ذخیره شماره کانفیگ فعلی
state_file = 'current_state.txt'

# تابع برای پیدا کردن کانفیگ بعدی
def get_next_config():
    if not os.path.exists(state_file):
        return configs[0], 0  # اگر فایل وضعیت وجود نداشت، از کانفیگ اول شروع کنید

    with open(state_file, 'r') as f:
        current_index = int(f.read().strip())

    next_index = (current_index + 1) % len(configs)
    return configs[next_index], next_index

# دریافت لینک کانفیگ بعدی
next_config_url, next_index = get_next_config()

# دریافت محتوای کانفیگ از فایل txt
response = requests.get(next_config_url)
next_config_content = response.text.strip()

# نوشتن محتوای جدید در فایل main.txt
with open('main.txt', 'w') as f:
    f.write(next_config_content)

# ذخیره وضعیت جدید
with open(state_file, 'w') as f:
    f.write(str(next_index))

print(f"Updated main.txt with content from: {next_config_url}")
