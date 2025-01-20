import datetime
from collections import defaultdict
import os

def analyze_apache_log(log_file_path, output_file_path):
    # Проверяем, существует ли файл
    if not os.path.exists(log_file_path):
        print(f"Файл {log_file_path} не найден.")
        return

    # Словарь для хранения количества событий за каждый час
    event_count = defaultdict(int)

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            # Разберем строку лога
            parts = line.strip().split('[')
            if len(parts) < 2:
                continue
            event_time_str = parts[1].split(']')[0]
            event_time = datetime.datetime.strptime(event_time_str, '%d/%b/%Y:%H:%M:%S %z')

            # Обрезаем время до часа
            hour_key = event_time.strftime('%Y-%m-%d %H')

            event_count[hour_key] += 1

    # Записываем результаты в файл
    with open(output_file_path, 'w') as output_file:
        for hour, count in event_count.items():
            output_file.write(f"{hour}: {count}\n")

    return output_file_path

# Укажите пути до файла с логами и файла для вывода
log_file_path = 'logs/apache_log'  # Используйте доступный файл с логами
output_file_path = 'logs/apache_events_by_hour.txt'

processed_file_path = analyze_apache_log(log_file_path, output_file_path)
print(f"Обработанные данные записаны в файл: {processed_file_path}")
