import os
filename = "MyPi License"
os.chmod(filename, 0o444)
filename = "Install.sh"
os.chmod(filename, 0o000)
print("Done.")
