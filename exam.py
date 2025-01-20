import os

def parse_logs(input_file, output_file):
    """Считывает файл логов, подсчитывает коды 404 за каждую минуту и записывает результат."""
    with open(input_file) as f:
        with open(output_file, "w") as out:
            counter = 0
            last_min = -1
            for line in f:
                if ' 404 ' in line and '[' in line:
                    try:
                        minute = int(line[18:20])
                        if last_min != minute:
                            if last_min != -1:
                                out.write(f"Minute {last_min}: {counter} errors\n")
                            last_min = minute
                            counter = 0
                        counter += 1
                    except ValueError:
                        continue
            if last_min != -1:
                out.write(f"Minute {last_min}: {counter} errors\n")


def main():
    """Основная функция для вызова логики."""
    input_file = f"{os.getcwd()}/logs/nginx_log"
    output_file = f"{os.getcwd()}/output_404_count.txt"
    print(f"Processing logs from '{input_file}'...")
    parse_logs(input_file, output_file)
    print(f"Results written to '{output_file}'.")


if __name__ == "__main__":
    main()