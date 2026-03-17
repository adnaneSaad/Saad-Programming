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
