# Processes and signals
- A project during my Full Stack Software Engineering studies at [ALX Africa](https://www.alxafrica.com/software-engineering-2022/), a course offered by [Holberton School](https://www.holbertonschool.com/). 

## Technologies 

- Files written in ```vi```, ```vim```, and ```emacs``` editors. 
- C files compiled using ```gcc 9.4.0```.
- C files wriiten according to the betty coding style. Checked using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl).
- Bash scripts tested on ```Ubuntu 20.04```.
- Shell scripts cheked with [Shellcheck](https://github.com/koalaman/shellcheck).

## Files

| File  | Description/Question |
|-------|-----------------------|
|[0-what-is-my-pid](0-what-is-my-pid)|A Bash script that displays its own PID.|
|[1-list_your_processes](1-list_your_processes)| Bash script that displays a list of currently running processes.|
 |[2-show_your_bash_pid](2-show_your_bash_pid)| Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process. Uses [1-list_your_processes](1-list_your_processes)|
|[3-show_your_bash_pid_made_easy](3-show_your_bash_pid_made_easy)|Bash script that displays the PID, along with the process name, of processes whose name contain the word ```bash```.|
|[4-to_infinity_and_beyond](4-to_infinity_and_beyond)|A Bash script that displays ```To infinity and beyond``` indefinitely.|
|[5-dont_stop_me_now](5-dont_stop_me_now)| Bash script that stops [4-to_infinity_and_beyond](4-to_infinity_and_beyond) process.|
|[6-stop_me_if_you_can](6-stop_me_if_you_can)| A Bash script that stops [4-to_infinity_and_beyond](4-to_infinity_and_beyond) process.|
|[7-highlander](7-highlander)| A Bash script that displays: ```To infinity and beyond``` indefinitely. With a ```sleep 2`` in between each iteration. ```I am invincible!!!``` when receiving a SIGTERM signal.|
|[8-beheaded_process](8-beheaded_process)|Bash script that kills the process [7-highlander](7-highlander).|
|[100-process_and_pid_file](100-process_and_pid_file)| A Bash script that: Creates the file ```/var/run/myscript.pid``` containing its PID. Displays ```To infinity and beyond``` indefinitely. Displays ```I hate the kill command``` when receiving a SIGTERM signal. Displays ```Y U no love me?!``` when receiving a SIGINT signal. Deletes the file ```/var/run/myscript.pid``` and terminates itself when receiving a SIGQUIT or SIGTERM signal.|
|[manage_my_process](manage_my_process)|A Bash script that: Indefinitely writes ```I am alive!``` to the file ```/tmp/my_process```. In between every ```I am alive!``` message, the program should pause for 2 seconds. |
|[101-manage_my_process](101-manage_my_process)| A bash (init) script  that manages [manage_my_process](manage_my_process).|
|[102-zombie.c](102-zombie.c)|| A C program that creates 5 zombie processes. For every zombie process created, it displays Zombie process created, PID: ZOMBIE_PID|
