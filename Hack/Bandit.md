# 🚩 Bandit Wargame Passwords

|Level|Transition| Password                           |
|:---:| :------: |  :------------------------------:  |
| 0   | 0 -> 1   | `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If` |
| 1   | 1 -> 2   | `263JGJPfgU6LtdEvgfWU1XP5yac29mFx` |
| 2   | 2 -> 3   | `MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx` |
| 3   | 3 -> 4   | `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ` |
| 4   | 4 -> 5   | `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw` |
| 5   | 5 -> 6   | `HWasnPhtq9AVKe0dmk45nxy20cvUa6EG` |
| 6   | 6 -> 7   | `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj` |
| 7   | 7 -> 8   | `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc` |
| 8   | 8 -> 9   | `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM` |
| 9   | 9 -> 10  | `FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey` |
| 10  | 10 -> 11 | `dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr` |
| 11  | 11 -> 12 | `7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4` |
| 12  | 12 -> 13 | `FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn` |
| 13  | 13 -> 14 | `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS` |
| 14  | 14 -> 15 | `8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo` |
| 15  | 15 -> 16 | `kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx` |
| 16  | 16 -> 17 | `via bandit17.key(RSA Private Key)`|
| 17  | 17 -> 18 | `x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO` |
| 18  | 18 -> 19 | `cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8` |
| 19  | 19 -> 20 | `0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO` |
| 20  | 20 -> 21 | `EeoULMCra2q0dSkYj561DX7s1CpBuOBt` |
| 21  | 21 -> 22 | `tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q` |
| 22  | 22 -> 23 | `0Zf11ioIjMVN551jX3CmStKLYqjk54Ga` |
| 23  | 23 -> 24 | `gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8` |
| 24  | 24 -> 25 | `iCi86ttT4KSNe1armKiwbQNmB3YJP3q4` |
| 25  | 25 -> 26 | `via bandit26.sshkey`              |
| 26  | 26 -> 27 | `upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB` |
### HTB: Fawn
- **Target IP:** 10.129.52.141
- **Service:** FTP (Port 21)
- **Access Method:** Anonymous Login
- **Flag Captured:** 035db21c881520061c53e0536e44f815
- **Date:** 2026-03-23

---
### HTB: Dancing
- **Target IP:** 10.129.52.167
- **Service:** SMB (Port 445)
- **Access Method:** Null Session (-N) on WorkShares
- **Flag Captured:** 
- **Notes:** Found flag in James.P folder. Worknotes mention WinRM.
- **Date:** 2026-03-23

---

---
## 🧭 NAVIGATING THE REDIS WAREHOUSE (The Bandit Way)

### 1. The Entry (The Connection)
$ redis-cli -h [TARGET_IP]

### 2. Identifying the Aisle (Which DB?)
- **Check the Warehouse Layout:** `INFO keyspace`
  - *Look for "db0", "db1", etc. It tells you where the keys actually are.*
- **Move to an Aisle:** `SELECT 0` (or 1, 2, etc.)

### 3. Finding the Boxes (Keys)
- **Show EVERYTHING:** `KEYS *`
- **Pattern Search:** `KEYS flag*` (Finds: flag, flag1, flag_secret)
- **Search for Users:** `KEYS *user*` (Finds: superuser, user_pass, newuser)

### 4. Opening the Box (The Data)
- **Read a String:** `GET [key_name]`
- **Check the Type of Data:** `TYPE [key_name]` 
  - *If it says "string", use GET. If it says "list", use LRANGE.*

### 5. Cleaning Up
- **Clear the Terminal:** `CLEAR` (within the redis-cli prompt)
- **Exit:** `exit` or `QUIT`

---
### HTB: Appointment
- **Target IP:** 10.129.50.132
- **Service:** HTTP (Port 80) / Apache 2.4.38
- **Access Method:** SQL Injection (SQLi)
- **Payload used:** ' OR 1=1 -- -
- **Flag Captured:** e3d0796d002a446c0e622226f42e9672
- **Date:** 2026-03-27
- Task 10: The 'Success' message word is 'Congratulations'.

---

## 🛡️ Machine: Appointment (Tier 1 - Web)
- **Vulnerability:** SQL Injection (SQLi)
- **Method:** Used `' OR 1=1 -- -` to bypass the login form.
- **Task 10:** The success message starts with 'Congratulations'.
- **Flag:** e3d0796d002a446c0e622226f42e9672

---

## 🐬 Machine: Sequel (Tier 1 - Database)
- **Vulnerability:** Misconfigured MySQL (No password for root).
- **Service Port:** 3306 (Standard MySQL port).
- **Access Command:** mysql -h [IP] -u root
- **Workflow:** 1. SHOW DATABASES; -> htb
    2. USE htb;
    3. SHOW TABLES; -> config
    4. SELECT * FROM config;
- **Flag:** 7b4bec00d1a39e3dd4e021ec3d915da8

✅ Sequel Machine: COMPLETED (2026-03-27)

---
## 🏆 HTB STARTING POINT LOG (March 2026)
### 🗄️ Machine: Sequel
- **IP:** 10.129.50.152
- **Service:** MariaDB (Port 3306)
- **Method:** Manual MySQL handshake (nmap hung).
- **Flag:** 7b4bec00d1a39e3dd4e021ec3d915da8
- **Status:** PWNED ✅

### 🐊 Machine: Crocodile
- **IP:** 10.129.52.226
- **Service:** FTP (Port 21) & HTTP (Port 80)
- **Method:** Anonymous FTP login -> Gobuster for /login.php -> Admin login.
- **Flag:** c7110277ac44d78b6a9fff2232434d16
- **Status:** PWNED ✅
✅ 2026-03-28: Crocodile PWNED. Flag: c7110277ac44d78b6a9fff2232434d16
# SESSION LOG: 2026-03-29

## Target Information
* **Target IP:** 10.129.54.184
* **OS:** Windows 10/Server
* **Status:** FULL COMPROMISE (Pwned)

## Credentials & Access
* **Captured User:** Mike
* **Captured Admin:** Administrator
* **Cracked Password:** badminton
* **Access Method:** Evil-WinRM

## Captured Flags
* **User Flag (Mike):** ea81b7afddd03efaa0945333ed147fac
* **Root Flag (Admin):** (Paste your final Administrator flag here)

## Security Audit & Privilege Findings
The machine was compromised via LLMNR poisoning. Post-exploitation revealed the following critical misconfigurations:
* **SeDebugPrivilege:** Enabled (Allowed memory dumping/manipulation).
* **SeImpersonatePrivilege:** Enabled (Vulnerable to token impersonation).
* **SeBackupPrivilege:** Enabled (Allowed reading any file on disk).

## Tools Used
* Responder (on wlan0)
* Hashcat (on NVIDIA T1200 GPU / Fedora 43)
* Evil-WinRM
