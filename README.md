
## Install State
```bash
    # 1
    python -m venv .venv
    # 2
    .venv/script/activate
    # 3
    pip install -r requirement.txt
```

## Build EXE file
```bash
    #Build To Exe
    pyinstaller --onefile --icon=icon.ico --distpath ./ app.py
```

>> ใส่คำที่ต้องการในไฟล์ `words.txt` (1 คำ : 1 บรรทัด)