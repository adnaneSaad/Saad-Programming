import subprocess

def brute_force():
    # Trying the most common range for these levels
    for key in range(1000, 10000):
        p = subprocess.Popen(['./level15'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # We send the key and capture the output
        stdout, stderr = p.communicate(input=str(key))
        
        # If the output doesn't contain "Wrong", we found it!
        if "Wrong" not in stdout:
            print(f"[*] SUCCESS! Key found: {key}")
            print(f"[*] Output: {stdout}")
            break
        
        if key % 500 == 0:
            print(f"[-] Still searching... currently at {key}")

if __name__ == "__main__":
    brute_force()
