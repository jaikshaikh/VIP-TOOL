import time

text = "Bas kardo chutiyo, file khatam ho chuki hai..."
for char in text:
    print(char, end="", flush=True)
    time.sleep(0.1)  # Adjust the speed of typing effect

print()  # Move to the next line after printing the message