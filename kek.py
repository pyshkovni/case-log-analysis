import re
import os
from collections import defaultdict
from datetime import datetime

# Функция для обработки лога и подсчета количества ошибок 404 для каждой минуты
def parse_nginx_log(file_path):
    with open(file_path, 'r') as file:
        log_data = file.readlines()

    # Регулярное выражение для извлечения данных из строки лога
    log_pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}) \+\d{4}\] ".*" (\d{3}) .*'

    error_counts = defaultdict(int)

    for line in log_data:
        match = re.match(log_pattern, line)
        if match:
            timestamp = match.group(2)
            status_code = match.group(3)

            # Преобразуем метку времени в формат "год-месяц-день часы:минута" (игнорируем секунды)
            timestamp = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S").strftime("%Y-%m-%d %H:%M")

            # Подсчитываем количество ошибок 404
            if status_code == "404":
                error_counts[timestamp] += 1

    return error_counts

# Функция для сохранения результатов в файл
def save_error_counts_to_file(error_counts, output_file):
    with open(output_file, 'w') as file:
        for timestamp, count in sorted(error_counts.items()):
            file.write(f"{timestamp} - Ошибки 404: {count}\n")

# Главная функция для обработки лога и сохранения результатов
def main():
    log_file = f'{os.getcwd()}/logs/nginx_log'  # Замените путь на путь вашего файла
    output_file = f'{os.getcwd()}/404_errors_per_minute.txt'

    error_counts = parse_nginx_log(log_file)
    save_error_counts_to_file(error_counts, output_file)
    print(f"Результаты сохранены в {output_file}")

# Выполнение скрипта
if __name__ == "__main__":
    main()