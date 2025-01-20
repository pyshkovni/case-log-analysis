import datetime
from collections import defaultdict
import os

def process_apache_log(input_file, output_file):
    # Проверка наличия файла
    if not os.path.isfile(input_file):
        print(f"Файл {input_file} не найден.")
        return

    # Создание словаря для подсчета событий по часам
    hourly_events = defaultdict(int)

    with open(input_file, 'r') as log_data:
        for log_line in log_data:
            # Разбор строки лога
            log_parts = log_line.strip().split('[')
            if len(log_parts) < 2:
                continue
            time_string = log_parts[1].split(']')[0]
            log_time = datetime.datetime.strptime(time_string, '%d/%b/%Y:%H:%M:%S %z')

            # Обрезка времени до часа
            hour_key = log_time.strftime('%Y-%m-%d %H')

            hourly_events[hour_key] += 1

    # Запись результатов в файл
    with open(output_file, 'w') as result_file:
        for hour, event_count in hourly_events.items():
            result_file.write(f"{hour}: {event_count}\n")

    return output_file

# Укажите пути до файла с логами и файла для вывода
input_log_path = f'{os.getcwd()}/logs/apache_log'  # Используйте доступный файл с логами
output_log_path = f'{os.getcwd()}/apache_events_by_hour.txt'

process_apache_log(input_log_path, output_log_path)