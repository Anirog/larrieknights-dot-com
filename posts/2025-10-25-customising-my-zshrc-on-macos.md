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

🔧 My current `.zshrc`

    # 🧭 Navigation
    alias ..="cd .."
    alias desk="cd ~/Desktop"
    alias docs="cd ~/Documents"
    alias dl="cd ~/Downloads"

    # ⚙️ Quick utilities
    alias c="clear"
    alias ez="nano ~/.zshrc" # edit zshrc
    alias sz="cp ~/.zshrc ~/Documents/double-struck/.zshrc.backup && source ~/.zshrc" # backup and reload zshrc

    # 🐍 Python
    alias ds="python3 ~/Documents/double-struck/double_struck.py"

    # 🧠 Git shortcuts
    alias gs="git status"
    alias ga="git add ."
    alias gp="git push"
    alias gl="git pull"

    # This function processes the input data and returns the result.
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

    # 💫 Prompt: show current folder and branch (if inside a repo)
    autoload -U colors && colors
    setopt PROMPT_SUBST PROMPT_CR
    PROMPT='%F{cyan}%~%f %F{yellow}$(git branch --show-current 2>/dev/null)%f
    › '

    # 📂 Get a text file containing all the files in the current folder
    alias sl="find . -type f -maxdepth 1 | sed 's|^\./||' > ~/Desktop/file-list.txt"

    # 💫 Prompt: show current folder and branch (if inside a repo)
    autoload -U colors && colors
    setopt PROMPT_SUBST PROMPT_CR
    PROMPT='%F{cyan}%~%f %F{yellow}$(git branch --show-current 2>/dev/null)%f
    › '

    # 📂 Get a text file containing all the files in the current folder
    alias sl="find . -type f -maxdepth 1 | sed 's|^\./||' > ~/Desktop/file-list.txt"


## ✨ Highlights

**Shortcuts to jump around**

- `desk` takes me straight to `~/Desktop`
- `..` moves me up one folder

**Quick Git**

- `ga` for `git add .`
- `gc` to prompt for a commit message (or auto-generate one) use with:

`gc` or `gc "my message"`

- Saves loads of typing

**A custom prompt**

- Shows the current folder path in cyan
- Shows the Git branch in yellow if I'm inside a repo
- Adds a nice little `›` prompt symbol

**Simple automation**

- `sl` exports a list of files in the current folder to my Desktop
- `ds` runs a Python script I wrote from anywhere

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