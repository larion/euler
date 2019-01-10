tar -cvz --exclude-vcs problems | openssl enc -aes-256-cbc -e > euler.tar.gz.enc
