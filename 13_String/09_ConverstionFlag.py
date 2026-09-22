text = 'Hello\nWorld'
print(f'{text}')    # Hello
                    # World   (newline rendered)
print(f'{text!r}')  # 'Hello\nWorld'  — repr(): shows escape sequences
print(f'{text!s}')  # Hello\nWorld    — str(): same as default
print(f'{text!a}')  # 'Hello\nWorld'  — ascii(): escapes non-ASCII chars


# Unicode example with !a
name = 'Aarav'
print(f'{name!a}')   # 'Aarav'  — ASCII chars same
emoji = 'Python 🐍'
print(f'{emoji!a}')  # 'Python \U0001f40d'  — non-ASCII escaped