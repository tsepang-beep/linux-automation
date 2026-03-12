import subprocess

commands = [
        "sudo dnf update -y",
        "sudo dnf install wget -y",
        "sudo rpm -Uvh http://rpms.litespeedtech.com/centos/litespeed-repo-1.3-1.el.noarch.rpm",
        "sudo dnf install openlitespeed -y",
        "sudo systemctl start lsws",
        "sudo systemctl enable lsws"
        ]
      for command in commands:

          print("Running:", command)

          try:

              result = suprocess.run(command, shell=True, check=True,
                      stdout=suprocess.PIPE,
                      stderr=subprocess.PIPE,
                      text=True)

              print("SUCCESS")
              print(result.stdout)

          except subprocess.CalledProcessError as error:

              print("ERROR:", error.stderr)
              break
