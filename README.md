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

`hello delete` the 'hello' text is deleted from your secret vault.

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

### how to run this program

* Fork or download this repo.
* `cd` into the folder where you downloaded the file
* Then, if you're on Windows, and assuming you have some text in your clipboard you want to save, run:

```
python multiclip.py <key> <operation>
```
Replace`key` with the name you want to use to identify the text and `operation` with what you want to do with the text (choices are `save`, `load`, and `delete`)

On Linux or Mac, run
```
python3 multiclip.py <key> <operation> 
```
Replace`key` with the name you want to use to identify the text and `operation` with what you want to do with the text (choices are `save`, `load`, and `delete`).

### Things to Improve
---

- An optional `--list` argument that returns a list of the keys you have saved in your vault. Please fork this repo, add the feature, and submit a pull request. 

- The help message. The text that’s printed when you run the `--help` command is not properly formatted. The help text for each argument should appear on a new line to improve readability. 

> [!WARNING]
>  Many tools do exactly what Multiclip does and more. This is just a casual project, though important to me, so expect many flaws. I’m sure you’ll find lots of ways to help improve the code and add more useful features. Feel free to fork the repo and do your thing. 

Multiclip was inspired by a project idea in chapter 7 of Al Sweigart's [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/). Al is also the author of `Pyperclip`



