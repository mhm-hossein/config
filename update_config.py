# لیست لینک‌های کانفیگ‌ها
configs = [
    "https://raw.githubusercontent.com/mhm-hossein/config/main/list1",
    "https://raw.githubusercontent.com/mhm-hossein/config/main/list1",
    # ادامه لینک‌ها
]

# تابع برای پیدا کردن لینک بعدی
def get_next_config(current_config):
    try:
        current_index = configs.index(current_config)
        next_index = (current_index + 1) % len(configs)  # نوبتی شدن لینک‌ها
        return configs[next_index]
    except ValueError:
        return configs[0]  # اگر لینک فعلی پیدا نشد، لینک اول را برگردانید

# خواندن فایل main.txt
with open('main.txt', 'r') as f:
    current_config = f.read().strip()

# پیدا کردن لینک بعدی
next_config = get_next_config(current_config)

# نوشتن لینک جدید در فایل main.txt
with open('main.txt', 'w') as f:
    f.write(next_config)

print(f"Updated config to: {next_config}")
