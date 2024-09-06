import json

# لیست لینک‌های کانفیگ‌ها
configs = [
    "https://raw.githubusercontent.com/mhm-hossein/config/main/list1",
    "https://raw.githubusercontent.com/mhm-hossein/config/main/list2",
    
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

# خواندن فایل main.json
with open('main.json', 'r') as f:
    data = json.load(f)

current_config = data['config_url']

# پیدا کردن لینک بعدی
next_config = get_next_config(current_config)

# به‌روزرسانی فایل main.json با لینک جدید
data['config_url'] = next_config

# نوشتن تغییرات در فایل main.json
with open('main.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f"Updated config to: {next_config}")
