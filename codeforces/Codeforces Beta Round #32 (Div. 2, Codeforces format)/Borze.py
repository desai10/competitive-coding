inp = input()

buf = ''

outp = ''

for c in inp:
    if buf == '':
        if c == '.':
            outp += '0'
        else:
            buf += c
    else:
        if c == '.':
            outp += '1'
        else:
            outp += '2'
        buf = ''

print (outp)