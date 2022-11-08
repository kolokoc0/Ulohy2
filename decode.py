def decode (text,key):
  poc = -1
  vys = ""
  temp = 0
  for i in text:
    poc += 1
    if i.isupper():
      temp = 65
    else:
      if i.islower():
        temp=97
    hod = ord(i)-temp
    hod2 = (ord(key[poc%len(key)]))-97
    change = (hod-hod2) -1
    change = change %26
    change = change + temp
    if ord(i)==32:
      vys += " "
    else:
      vys += chr(change)
  return vys
print(decode("Ldtd oaye", "kvet"))
 