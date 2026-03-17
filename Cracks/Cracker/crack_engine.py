#!/usr/bin/env python3
import subprocess
import sys

def universal_crack(target):
    print(f"[*] Analyzing {target} on Fedora 43 (i7-11th Gen)...")
    
    for key in range(256):
        try:
            # Run with a short timeout to catch infinite loops
            # 2>&1 merges stderr into stdout so we see crash messages
            p = subprocess.Popen([target], stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                                 stderr=subprocess.STDOUT, text=True)
            
            output, _ = p.communicate(input=str(key) + "\n", timeout=0.2)
            
            # CRITERIA FOR SUCCESS:
            # 1. The program actually says "SUCCESS" or "Flag"
            # 2. The program exits cleanly (returncode 0) and gave ANY output
            # 3. The output contains a '{' (often part of a flag)
            if any(word in output.upper() for word in ["SUCCESS", "FLAG", "CONGRAT"]) or \
               (p.returncode == 0 and len(output.strip()) > 0) or \
               "{" in output:
                
                print(f"\n[✔] MATCH FOUND!")
                print(f"  > Key:    {key}")
                print(f"  > Output: {output.strip()}")
                return

        except subprocess.TimeoutExpired:
            p.kill()
        except Exception:
            continue

        if key % 20 == 0:
            print(f"  Testing keys... {key}/255", end="\r")

    print("\n[!] No valid key identified. Possible anti-debugging or custom XOR detected.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: crackit <binary>")
    else:
        universal_crack(sys.argv[1])
