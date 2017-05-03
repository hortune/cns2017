./rsatool-master/rsatool.py $(python solution.py) -o private.pem
openssl rsautl -decrypt -inkey private.pem -in flag.enc -out flag.bin
cat flag.bin
