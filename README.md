# Multiclip

**Multiclip** is a simple command line tool for managing your clipboard history. Use it to save multiple text to your clipboard, load specific text from the clipboard, or delete text you no longer need. Multiclip is your trusty clipboard history manager. 

The program responds to the following few commands:

### save
---

* `<key> save` saves text copied to your clipboard with the unique identifier you provide. The key can be any string. 

Example: 

`hello save` will save the text in your clipboard to a secret dictionary-like database using the word 'hello' as the key and the copied text as the value.

### load

* `<key> load` retrieves text previously saved under `<key>` and pastes it back into your clipboard.

Example:

```
hello load
```

text associated with the keyword 'hello' is copied back to your clipboard and displayed on the screen. 

### delete

`<key> delete` clears text saved to `<key>` in your vault.

Example usage:

`hello delete` the 'hello' text is deleted from your seceret vault.

### help

Like most command line tools, running  the help command (`--help`) will print a help message to the screen. 

On Windows, the command will look like this (assuming you’re in the project directory):

`python multiclip.py --help`

On Linux and Mac, it would be:

`python3 multiclip.py --help`.

> [!NOTE]
> Multiclip was tested only on Windows. But it should work fine for Linux and macOS

### Running Multiclip

The program utiliies arparse, shelve, and pypeclip modules argpase and shelve are standard libraries, so you need not install them. But you have to install pyperclip, a third party module for saving and pasting clipboard text. On Windows, run

`python -m pip install pyperclip`

On Linux, run

`sudo pip3 install pyperclip`

On mac, run

`pip3 install pyperclip`












