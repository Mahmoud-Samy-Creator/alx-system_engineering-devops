# 0x04. Loops, conditions and parsing

## General
* How to create SSH keys
* What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
* How to use while, until and for loops
* How to use if, else, elif and case condition statements
* How to use the cut command
* What are files and other comparison operators, and how to use them

## Requirements
### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* You are not allowed to use awk
* Your Bash script must pass Shellcheck (version 0.7.0) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## Bash scripts
* 1-for_best_school - Displays Best School 10 times. [for loop]

* 2-while_best_school - Displays Best School 10 times. [while loop]

* 3-until_best_school - Displays Best School 10 times. [until loop]

* 4-if_9_say_hi - Displays Best School 10 times with 'Hi' at 9th iteration

* 5-4_bad_luck_8_is_your_chance - Loops from 1 to 10:
- Displays 'bad luck' for the 4th loop iteration
- Displays 'good luck' for the 8th loop iteration
- Displays 'Best School' for the other iterations

* 6-superstitious_numbers - Displays numbers from 1 to 20 and:
- Displays '4' and then 'bad luck from China' for the 4th loop iteration
- Displays '9' and then 'bad luck from Japan' for the 9th loop iteration
- Displays '17' and then 'bad luck from Italy' for the 17th loop iteration

* 7-clock - Displays the time for 12 hours and 59 minutes: [while loop]
- Display hours from 0 to 12
- Display minutes from 1 to 59

* 8-for_ls - Display the content of the current directory In a list format Where only the part of the name after the first dash is displayed [for loop]

* 9-to_file_or_not_to_file - Gives you information about the school file:
- Check if the file exists and print:
- if the file exists: school file exists
- if the file does not exist: school file does not exist
- if the file exists, print:
- if the file is empty: school file is empty
- if the file is not empty: school file is not empty
- if the file is a regular file: school is a regular file
- if the file is not a regular file: (nothing)

* 10-fizzbuzz - Displays numbers from 1 to 100 in list format:
- Displays FizzBuzz when the number is a multiple of 3 and 5
- Displays Fizz when the number is multiple of 3
- Displays Buzz when the number is a multiple of 5
- Otherwise, displays the number

* 100-read_and_cut - Displays the content of the file /etc/passwd: [while loop]
- Your script should only display:
- username
- user id
- Home directory path for the user

* 101-tell_the_story_of_passwd - A script tells a story using /etc/passwd file