import pexpect
import sys

log_file = open("session_log.txt", "w", encoding="utf-8")

class Logger:
    def write(self, data):
        sys.stdout.write(data)
        log_file.write(data)

    def flush(self):
        sys.stdout.flush()
        log_file.flush()

print("Welcome to the auto downloader")

child = pexpect.spawn("ani-cli", encoding="utf-8")
child.logfile = Logger()

userin = input("Enter what show you would like to download: ")

child.expect("Search", timeout=10)
child.sendline(userin)

child.expect("Select", timeout=10)
child.sendline("1")
child.sendline("\r")
child.sendline("")

#episode = 69
#print(f"{userin} has {episode}")

#user_range_start = int(input("Enter the episode to start at: "))
#user_range_end = int(input("Enter the episode to end at: "))

child.expect("Select episode", timeout=10)
child.sendline(str(9))

child.expect(pexpect.EOF)

print("Done")