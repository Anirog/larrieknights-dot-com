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

# 💻 Terminal (alias) commands

## 🧭 Navigation

<kbd>..</kbd> - Moves up one folder

<kbd>desk</kbd> - Go to `Desktop`

<kbd>docs</kbd> - Go to `Documents`

<kbd>dl</kbd> - Go to `Downloads`

<kbd>finder</kbd> - Open current folder in Finder

## ⚙️ Quick utilities

<kbd>c</kbd> - Clear the terminal

<kbd>ez</kbd> - Open `.zshrc` in nano for editing

<kbd>sz</kbd> - Backup `.zshrc` and reload it

<kbd>cpwd</kbd> - Copy current directory path to clipboard

## 🐍 Python

<kbd>ds</kbd> - Run `double_struck.py`

<kbd>zen</kbd> - Run `zen_quote.py`

## 🧠 Git shortcuts

<kbd>gc</kbd> - Git commit with auto-generated message

<kbd>gp</kbd> - Git push

<kbd>gs</kbd> - Git status

<kbd>ga</kbd> - Git add all changes

<kbd>gl</kbd> - Git pull

<kbd>glg</kbd> - View a compact graphical git log

## 📂 File listing

<kbd>sl</kbd> - Save a file list of the current folder to your Desktop

## 🛜 Network

<kbd>ip</kbd> - Show local IP address

## 🎲 Modifiers

<kbd>ls</kbd> -Show files with type indicators

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