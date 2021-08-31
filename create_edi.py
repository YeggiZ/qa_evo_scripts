#-*- coding: utf-8 -*-
#!/usr/bin/python3
import os
import sys


def log(text):
    print(text)

def get_schemas(name):
    home_dir = os.getcwd()
    available_schemas = os.listdir(f'{home_dir}/schemas')

    if name.lower() in available_schemas:
        log(f'The Shaema for document type "{name}" is in available schemas')
    else:
        log(f'The Shaema for document type "{name}" is in NOT available')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_schemas(sys.argv[1])
    else:
        log('Empty request')
    