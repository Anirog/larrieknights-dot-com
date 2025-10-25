---
title: Customising my .zshrc on macOS
date: 2025-10-25
slug: 2025-10-25-customising-my-zshrc-on-macos
tags: [macos, coding, python, terminal, productivity]
image: https://ik.imagekit.io/1wh3oo1zp/customising-my-zshrc-on-macos_mgdWuCAPK
image_alt: Customising my .zshrc on macOS
---

# Customising my .zshrc on macOS

I’ve been refining my terminal workflow on macOS by adding helpful aliases and a more pleasant prompt. As a bonus, I’ve also set up a small Python script that I can run from anywhere, which feels like a real enhancement.


If you'd like to do something similar, here's how I set up my `.zshrc` configuration.

## 🛠️ What is `.zshrc`?

`.zshrc` is a hidden configuration file that loads every time you open a new Terminal window. It's where you add aliases, tweak settings, and customise your prompt.

Think of it like your Terminal's personal preferences.

# ⌨️ Alias (shortcuts)

## 🧭 Navigation

- `..` moves me up one folder
- `desk` takes me straight to `~/Desktop`
- `docs` takes me straight to `~/Documents`
- `dl` takes me straight to `~/Downloads`

## ⚙️ Quick utilities

- `c` `clear`
- `ez` edit .zshrc in nano
- `sz` Backup and reload `.zshrc`

## 🐍 Python
- `ds` runs a Python script I wrote from anywhere

# 🧠 Git shortcuts
- `ga` for `git add .`
- `gs` for `git status`
- `gp` for `git push`
- `gl` for `git pull`
- `gc` for `git commit`

# 🪜 Optional Extras
- `sl` exports a list of files in the current folder to my Desktop
- `ds` runs a Python script I wrote from anywhere

# gc - or How I Learned to Stop Worrying and Love Commit Messages

For the `gc` alias it got slightly more complicated, as the `commit`command requires an input for the commit message.

like this `git commit -m "My commit message"`

So now when I type `gc` with no arguments, it automatically generates a commit message based on the changed files. If I provide a message like `gc "Fixed bug"`, it uses that instead.

Using this code snippet in my `.zshrc`:

```zsh
function gc () {
    if [ -z "$1" ]; then
        files=$(git status --short | awk '{print $2}' | xargs)
        if [ -z "$files" ]; then
            echo "Error: No changes to commit"
            return 1
        fi
        msg="commit: updated files: $files"
    else
        msg="commit: $1"
    fi
    git add .
    git commit -m "$msg"
}
```

**A custom prompt**

- Shows the current folder path in cyan
- Shows the Git branch in yellow if I'm inside a repo
- Adds a nice little `›` prompt symbol

![macOS Terminal](https://ik.imagekit.io/1wh3oo1zp/terminal_4TnKveg6O?updatedAt=1761419872138)

## ✅ How you can set this up

1. Open your `.zshrc` file

`nano ~/.zshrc`

If the file doesn't exist, that command will create it.

## 2. Paste in the aliases and prompt from above

Add them anywhere, but grouping them like I did keeps things tidy.

## 3. Save and reload

Press `CTRL + O` to save.  
Press `CTRL + X` to exit Nano.

Then reload your config:

`source ~/.zshrc`

(That's what my `sz` alias does.)

## 🐍 Adding a custom Python script (optional but fun)

I made a small Python script called **double_struck.py** and saved it here:

`~/Documents/double-struck/double_struck.py`

Then I added this alias:

`alias ds="python3 ~/Documents/double-struck/double_struck.py"`

Now typing:

`ds`

Runs my script instantly from anywhere.

## 🎯 Final thoughts

Making your own `.zshrc` is one of those tiny improvements that quietly pays off every day. It keeps my terminal fast, organised, and a bit more _me_.

If you haven't customised yours yet, start small: one shortcut that saves you time, then build from there.

[GitHub Repo](https://github.com/Anirog/zshrc)