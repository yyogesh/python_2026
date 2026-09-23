├── README.md
├── requirements.txt
├── .gitignore
├── main.py # entry file 
└── todo/ # src code 
    ├── __init__.py
    ├── tasks.py
    └── storage.py


python main.py add "Buy milk" --priority high --due 2026-09-10
python main.py list --sort priority
python main.py done 2
python main.py remove 3