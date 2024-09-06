import requests

# لیست فایل‌های کانفیگ (به جای لینک، محتویات آن‌ها خوانده می‌شود)
configs = [
    "https://raw.githubusercontent.com/mhm-hossein/config/main/list1.txt",
    "https://raw.githubusercontent.com/mhm-hossein/config/main/list1.txt",
    # ادامه فایل‌ها
]

# تابع برای پیدا کردن لینک بعدی
def get_next_config(current_config):
    try:
        current_index = configs.index(current_config)
        next_index = (current_index + 1) % len(configs)  # نوبتی شدن کانفیگ‌ها
        return configs[next_index]
    except ValueError:
        return configs[0]  # اگر لینک فعلی پیدا نشد، کانفیگ اول را برگردانید

# خواندن فایل main.txt
with open('main.txt', 'r') as f:
    current_config = f.read().strip()

# پیدا کردن لینک فایل کانفیگ بعدی
next_config_url = get_next_config(current_config)

# دریافت محتوای کانفیگ از فایل txt
response = requests.get(next_config_url)
next_config_content = response.text.strip()

# نوشتن محتوای جدید در فایل main.txt
with open('main.txt', 'w') as f:
    f.write(next_config_content)

print(f"Updated main.txt with content from: {next_config_url}")
