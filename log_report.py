import os
from datetime import datetime

logs = ["/var/log/messages","/var/log/secure"]

report = "log_report.html"

html = "<html><body>"
html += "<h1>Linux Server Log Report</h1>"
html += "<p>Generated: " + str(datetime.now()) + "</p>"

for log in logs:

    if os.path.exists(log):

        html += "<h2>" + log + "</h2>"
        html += "<pre>"

        with open(log) as f:
            lines = f.readlines()

            for line in lines[-20:]:
                html += line

                html += "</pre>"

            else:

                html += "<p>Log not found: " + log + "</p>"

                html += "</body></html>"

                with open(report, "w") as f:
                    f.write(html)

                    print("HTML report created:", report)

