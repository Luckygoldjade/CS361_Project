#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from InquirerPy import inquirer
from InquirerPy.prompts import ListPrompt
# sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from clint.textui import prompt, puts, colored
from tst9_scrape_020524_v04 import get_wsj_data

def main():
    choices = ["NYSE Up and Down Volume Percentage", "Nasdaq Up and Down Volume Percentage", "Exit"]

    question = ListPrompt(
        message="Select an option:",
        choices=choices,
    )

    result = question.execute()
    print(result)

    if result == "NYSE Up and Down Volume Percentage":
        print("You selected NYSE Up and Down Volume Percentage")
        get_wsj_data()
    elif result == "Nasdaq Up and Down Volume Percentage":
        print("You selected Nasdaq Up and Down Volume Percentage")
        get_wsj_data()
    elif result == "Exit":
        print("You selected Exit")

    # puts(colored.blue('Hi {0}. Install {1} {2} to {3}'.format(name, inst, language or 'nothing', path)))



if __name__ == '__main__':
    main()

