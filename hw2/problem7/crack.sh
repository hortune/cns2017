for i in $(seq 1 3000); 
    do echo -n "Absolute offset: $i -> "; 
    openssl asn1parse -in wtf.pem  -offset $i -length 261 2>/dev/null; 
done | grep -a INTEGER
