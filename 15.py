def parse_logs(input_file, output_file):
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
    input_file = "nginx_log.txt"
    output_file = "output_404_count.txt"
    print(f"Processing logs from '{input_file}'...")
    parse_logs(input_file, output_file)
    print(f"Results written to '{output_file}'.")

if __name__ == "__main__":
    main()
