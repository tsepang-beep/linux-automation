#Linux Server Automation and Log Reporting
## Overview
This repository contains Python automation scripts for managing a Linux Servers:

1. **OpenLiteSpeed Installation Script** ('openlitespeed_install.py')
2. -Automates the installation of the OpenLiteSpeed web server
3. -Configures firewall ports and enables the service

4. **System Log Automation Script** (log_report_auto_push.py')
5. -Collects essential system information :
6. -Uptime
7. -Disk Usage
8. -Memory Usage
9. -Cpu information
10. -Logged-in users
11. Top processes
12. -Generates a clean HTML report ('log_report.html')
13. -Automatically commits and pushes updates to Github

14. -------

15. ##Usage
16. ### 1. Clone the repository
17. ```bash
    git clone git@github.com:tsepang-beep/linux-automation.git
    cd linux-automation
