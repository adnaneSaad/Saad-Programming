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
