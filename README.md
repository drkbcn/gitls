# 🐍 Git Index File Lister

**Python script to list the files inside a `.git` `index` file.** Perfect for cases where `git ls-files` doesn't work due to incomplete dumps or damaged repositories!

## 🚀 About this Script

This script parses the `.git/index` file directly and lists all tracked files, bypassing `git` commands. Ideal for use in recovery situations, corrupted repos, or when you need direct access to file listings in the Git index.

### 🧰 Features

- Extracts and lists all file entries in the Git index.
- Avoids dependency on `git` CLI, perfect for incomplete repositories.
- Saves output to a `.txt` file, making it easy to analyze or share file lists.

## ⚙️ Usage

Run the script by specifying the path to the `.git/index` file and an output file name. Here’s how:

```bash
python lsgit.py /path/to/.git/index output.txt
```

### Example

```bash
python lsgit.py /home/user/project/.git/index file_list.txt
```

This command will generate a `file_list.txt` with all files listed in the Git index.

## 🛠 Requirements

- Python 3.x
- Works on any system with Python installed!

## 📄 Code Overview

The script:
1. Reads the `.git/index` file in binary mode.
2. Parses entries, capturing file paths in UTF-8.
3. Outputs the results to the specified text file.

Error handling ensures a smooth run even with non-UTF-8 characters or partially corrupted data.

## 👥 Contributing

Want to make it even better? Contributions are welcome! Simply fork the project, make your changes, and submit a pull request.

## 📜 License

This project is open-source under the MIT License. Feel free to use, modify, and distribute it as you like.

---

Let’s make Git indexing easier, one script at a time! 🚀
