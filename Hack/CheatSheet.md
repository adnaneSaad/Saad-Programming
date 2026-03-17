# Bandit Hackers Cheat Sheet

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
