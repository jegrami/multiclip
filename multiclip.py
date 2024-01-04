#!/usr/bin/python3

# Multiclip - a command line tool for saving and loading text to and from 
# the clipboard. 

import argparse
import pyperclip
import shelve

def save_text(key):
    '''A function to save text copied to clipboard'''
    data = pyperclip.paste() # pastes text from clipboard.
    with shelve.open('clipboard_data') as clipboard:
        clipboard[key] = data   # saves text in shelve object with the provided key.
        print(f'Saved text to {key}.')


def load_text(key):
    '''A function to load text saved to clipboard shelve'''
    with shelve.open('clipboard_data') as clipboard:
        if key in clipboard:
            data = clipboard[key] # loads text from shelve object using <key>
            pyperclip.copy(data)
            print(f'Text for {key}:\n{data}')
        else:
            print(f"You haven't yet saved any data for {key}.")

def list_keys():
    ''' A function to list the keys available in shelve'''
    with shelve.open('clipboard_data') as clipboard:
        keys = pyperclip.copy(str(list(clipboard.keys())))
        if keys:
            print(f"Keys you have saved in your clipboard:\n")
            for key in keys:
                print(f"- {key}")
        else:
            print('No keys found in clipboard.')


def delete_key(key):
    '''A function to delete saved text from shelve'''
    with shelve.open('clipboard_data') as clipboard:
        if key in clipboard:
            del clipboard[key]
            print(f"Deleted {key}.")


def main():
    text_parser = argparse.ArgumentParser(
        prog='Multiclip',
        description='''A command line tool for managing your clipboard history''',
        usage='%(prog)s [Options]'
    )
    text_parser.add_argument('key', help='key to save text to (or identify text in) clipboard')
    text_parser.add_argument('operation', choices=['save', 'load', 'delete'], 
                        help="Operations to perform on key:\
                            '<key> save' - saves copied text to clipboard.\
                                '<key> load' - loads text saved to <key> from clipboard.\
                                    '<key> delete' - deletes text saved to <key> from clipboard.")
    text_parser.add_argument('--list', action='store_true', help='List all keys saved to clipboard')

    args = text_parser.parse_args()

    if args.list:
        list_keys()
    elif args.operation == 'save':
        save_text(args.key)
    elif args.operation == 'load':
        load_text(args.key)
    elif args.operation == 'delete':
        delete_key(args.key)

if __name__ == '__main__':
    main()










