#!/user/bin/env python3
import subprocess
from datetime import datetime
import os

#-----Configuration----
report_file = "log_report.html"

repo_path = os.getcwd() #linux-automation
commit_message = f"Automated log update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# ---Functions---
def run_command(cmd):
 try:
    output = subprocess.getoutput(cmd)
 except Exception as e:
    output = str(e)
 return output

def collect_system_logs():
    """Collect system logs for report"""
    logs = {}
    logs["System Date & Time"] = str(datetime.now())
    logs["Uptime"] = run_command("uptime")
    logs["Disk Usage"] = run_command("df -h")
    logs["Memory Usage"] = run_command("free -h")
    logs["CPU Info"] = run_command("lscpu")
    logs["Logged Users"] = run_command("who")
    logs["Top Processes"] = run_command("top -b -n 5 | head -n 20")
    return logs

def generate_html_report(logs):
    """Generate HTML report from logs"""
    with open(report_file, "w") as f:
        f.write("<html><head><title>Linux Server Report</title></head><body>")
        f.write(f"<p>Generated: {logs['System Date & Time']}</p><hr>")
        for section, content in logs.items():
            if section == "System Date & Time":
                continue
            f.write(f"<h2>{section}</h2>")
            f.write(f"<pre>{content}</pre")
            f.write("</body></html>")
            print(f"Report generated: {os.path.abspath(report_file)}")

            def git_push_report():
                """Add, commit, and push report to Github"""
                print("\nUpdating Git repository...")
                commands = [
                        f"git add {report_file}",
                        f"git commit -m \"{commit_message}\"",
                        "git push origin main"
                        ]
                for cmd in commands:
                    result = subprocess.run(cmd, shell=True)
                    if result.returncode != 0:
                        print(f"Command failed: {cmd}")
                        break
                    print("Git push completed.")

                    # --- Main workflow ---
                    if _name_ == "_main_":
                        logs = collect_system_logs()
                        generate_html_report(logs)
                        git_push_report()
                        print("\nAll tasks completed successfully!")

