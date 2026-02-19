import os

filename = "MyPi License"
os.chmod(filename, 0o444)

filename = "README.md"
os.chmod(filename, 0o444)

print("Done.")
