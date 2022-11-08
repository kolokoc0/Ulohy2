def encode(text, key):
  vys = ""
  poc = -1
  temp = 0
  for i in text:
    if i.isupper():
      temp = 65
    else:
      if i.islower():
        temp = 97
    poc += 1
    hod = (ord(key[poc % len(key)])) - 97
    hod2 = (ord(i) - temp)
    change = hod + hod2 + 1
    change = change % 26
    change = change + temp
    if ord(i) == 32:
        vys += " "
    else:
        vys += chr(change)
  return vys


print(encode("Ahoj svet", "kvet"))