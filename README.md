# 🧾 Python Log Analyzer

A Python-based log analysis tool that reads log files, identifies log levels, extracts error messages, and generates a summary report.  
This project demonstrates practical log parsing, file handling, and DevOps-style troubleshooting.

---

## 🚀 Features

- Parses log files line by line
- Counts INFO, WARNING, and ERROR messages
- Extracts detailed error messages
- Generates a readable summary report
- Lightweight and beginner-friendly
- Easy to extend for real-world use

---

## 🛠️ Tech Stack

- Python 3
- File handling (`open`, `read`)
- OS module (`os`)

---

## 📂 Project Structure

## ▶️ How to Run

1️⃣ Make sure the log file exists:
logs/sample.log


2️⃣ Run the script:
```bash
python analyzer.py

📄 Sample Log File

INFO Application started successfully
WARNING Disk usage is high
ERROR Failed to connect to database
INFO Retrying connection
ERROR Database connection timeout


📊 Sample Output (report.txt)


📊 Log Analysis Report
----------------------
INFO messages    : 2
WARNING messages : 1
ERROR messages   : 2


❌ Error Details:
- ERROR Failed to connect to database
- ERROR Database connection timeout


📌 Use Cases

• Application log monitoring

• Debugging system issues

• DevOps & SRE practice

• Learning log parsing in Python

• Entry-level automation projects


🔮 Future Enhancements

• Support large log files

• Filter logs by date/time

• Export report as CSV

• Real-time log monitoring

Dockerize the analyzer


📄 License

• This project is open-source and intended for learning and educational purposes.
