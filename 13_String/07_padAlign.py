 # ljust / rjust / center — pad to a given width
s = 'Python'
print(s.ljust(15))           # 'Python         '  — left, pad right with spaces
print(s.rjust(15))           # '         Python'  — right, pad left with spaces
print(s.center(15))          # '    Python     '  — centred
print(s.center(15, '-'))     # '----Python-----'  — custom fill char
print(s.ljust(15, '*'))      # 'Python*********'  — custom fill char
# zfill — pad with zeros on the LEFT (useful for IDs, invoice numbers)
print('42'.zfill(8))         # '00000042'
print('INV'.zfill(8))        # '00000INV'
print('-42'.zfill(8))        # '-0000042'  — preserves sign!
