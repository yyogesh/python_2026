from pathlib import Path
# Creating Path objects

p1 = Path('/home/user/documents')   # absolute path
p2 = Path('data/expenses.json')     # relative path
p3 = Path.home()                    # current user's home directory
p4 = Path.cwd() 

data_dir = Path.home() / '.expense_tracker'
data_file = data_dir / 'expenses.json'
log_file  = data_dir / 'logs' / 'app.log'
print(data_file)

p = Path('/home/user/docs/report.pdf')
print(p.name)       # 'report.pdf'       — filename with extension
print(p.stem)       # 'report'           — filename without extension
print(p.suffix)     # '.pdf'             — extension including dot
print(p.parent)     # /home/user/docs    — parent directory
print(p.parts)      # ('/', 'home', 'user', 'docs', 'report.pdf')