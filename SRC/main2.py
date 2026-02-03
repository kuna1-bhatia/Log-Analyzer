import os

LOG_FILE = "logs/sample.log"
REPORT_FILE = "report.txt"

def analyze_logs():
    if not os.path.exists(LOG_FILE):
        print("Log file not found!")
        return 

    info_count = 0
    warning_count = 0
    error_count = 0
    error_messages = []

    with open(LOG_FILE, "r") as file:
        for line in file:
            if "INFO" in line:
                info_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "ERROR" in line:
                error_count += 1
                error_messages.append(line.strip())

    with open(REPORT_FILE, "w") as report:
        report.write("Log Analysis Report\n")
        report.write("----------------------\n")
        report.write(f"INFO messages    : {info_count}\n")
        report.write(f"WARNING messages : {warning_count}\n")
        report.write(f"ERROR messages   : {error_count}\n\n")

        report.write("Error Details:\n")
        for error in error_messages:
            report.write(f"- {error}\n")

    print("Log analysis completed. Report generated.")

if __name__ == "__main__":
    analyze_logs()
