import sys
import re
from typing import List, Dict, Callable


def parse_log_line(line: str) -> Dict[str, str]:
    # Parse a log line into a dictionary with components: date, time, level, message.
    match = re.match(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)", line)
    if match:
        return {
            "date": match.group(1),
            "time": match.group(2),
            "level": match.group(3),
            "message": match.group(4),
        }
    return {}


def load_logs(file_path: str) -> List[Dict[str, str]]:
    #    Load logs from a file and parse each line into a dictionary.
    logs = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        sys.exit(1)
    return logs


def filter_logs_by_level(
    logs: List[Dict[str, str]], level: str
) -> List[Dict[str, str]]:
    # Filter logs by level.
    return [log for log in logs if log["level"].upper() == level.upper()]


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    # Count logs by level.
    levels = ["INFO", "ERROR", "DEBUG", "WARNING"]
    counts = {level: 0 for level in levels}
    for log in logs:
        if log["level"] in counts:
            counts[log["level"]] += 1
    return counts


def display_log_counts(counts: Dict[str, int]):
    # Formatting and printing the results of the count in table format.
    print("Log level | Count")
    print("----------|-------")
    for level, count in counts.items():
        print(f"{level:9} | {count}")


def main():
    if len(sys.argv) < 2:
        print("How to use: python main.py /path/to/logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            print(f"\nLog details for level '{level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nLog details for level '{level.upper()}' not found.")


if __name__ == "__main__":
    main()
