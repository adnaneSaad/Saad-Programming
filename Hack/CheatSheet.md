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
