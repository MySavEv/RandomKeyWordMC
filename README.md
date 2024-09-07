
## Install State
```bash
    # 1
    python -m venv .venv
    # 2
    ./.venv/scripts/activate
    # 3
    pip install -r requirements.txt
```

## Build EXE file
```bash
    #Build To Exe
    pyinstaller --onefile --icon=icon.ico --distpath ./ app.py
```

## Note
- ใส่คำที่ต้องการในไฟล์ `words.txt` (1 คำ : 1 บรรทัด)
- หากจะให้มีการเว้นบรรทัดให้ ใช้ `\n` ขั้นกลาง