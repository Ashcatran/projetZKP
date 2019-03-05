./zokrates generate-proof | sed '/Point/!d;s/.*Point(\(.*\));/[\1],/g;s/\(0x[0–9a-f]*\)/"\1"/g;' | awk '{a=a s $0;s=" "}END{print a}'
