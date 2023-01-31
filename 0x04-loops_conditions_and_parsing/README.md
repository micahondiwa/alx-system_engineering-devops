# Loops, conditions and parsing

- A project during my Full Stack Software Engineering studies at [ALX Africa](https://www.alxafrica.com/software-engineering-2022/), a course offered by [Holberton School](https://www.holbertonschool.com/). 

## Technologies 

- Files written in ```vi```, ```vim```, and ```emacs``` editors. 
- C files compiled using ```gcc 9.4.0```.
- C files wriiten according to the betty coding style. Checked using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl).
- Bash scripts tested on ```Ubuntu 20.04```.
- Shell scripts cheked with [Shellcheck](https://github.com/koalaman/shellcheck).

## Files

| File  | Description/Question |
| ---  | --- |
|[0-RSA_public_key.pub](0-RSA_public_key.pub)| A file containing a SSH public key.|
|[1-for_best_school](1-for_best_school)|A Bash script that displays ```Best School``` 10 times using the ```for``` loop|. 
|[2-while_best_school](2-while_best_school)|A Bash script that displays ```Best School``` 10 times using the ```while``` loop.|
|[3-until_best_school](3-until_best_school)| Bash script that displays ```Best School``` 10 times using the ```until```.|
|[4-if_9_say_hi](4-if_9_say_hi)| Bash script that displays ```Best School 10``` times, but for the 9th iteration, displays ```Best School``` and then ```Hi``` on a new line using the ```while``` loop.|
|[5-4_bad_luck_8_is_your_chance](5-4_bad_luck_8_is_your_chance)|A Bash script that loops from 1 to 10 and: displays ```bad luck``` for the 4th loop iteration, displays ```good luck``` for the 8th loop iteration, displays ```Best School``` for the other iterations. Uses a ```while``` loop.|
|[6-superstitious_numbers](6-superstitious_numbers)|A  Bash script that displays numbers from 1 to 20 and: displays ```4``` and then ```bad luck from China``` for the 4th loop iteration, displays ```9``` and then ```bad luck from Japan``` for the 9th loop iteration,displays ```17``` and then ```bad luck from Italy``` for the 17th loop iteration. Uses ```while``` loop.|
|[7-clock](7-clock)|A Bash script that displays the time for 12 hours and 59 minutes: display hours from 0 to 12, display minutes from 1 to 59. Uses ```while``` loop.|
|[8-for_ls](8-for_ls)|A Bash script that displays: The content of the current directory, adn In a list format. Uses a ```for``` loop.|
|[9-to_file_or_not_to_file](9-to_file_or_not_to_file)|A Bash script that gives you information about the school file. Uses ```if``` and ```else```.|
|[10-fizzbuzz](10-fizzbuzz)|A Bash script that displays numbers from 1 to 100. Displays FizzBuzz when the number is a multiple of 3 and 5, Displays Fizz when the number is multiple of 3, Displays Buzz when the number is a multiple of 5, Otherwise, displays the number.In a list format.|
|[100-read_and_cut](100-read_and_cut)|A Bash script that displays the content of the file ```/etc/passwd```. The script  only display: username, user id, and Home directory path for the user.|
|[101-tell_the_story_of_passwd](101-tell_the_story_of_passwd)| A  Bash script that displays the content of the file ```/etc/passwd```, using the while loop + IFS.|
|[102-lets_parse_apache_logs](102-lets_parse_apache_logs)| A Bash script that displays the visitor IP along with the [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) from the Apache log file.|
|[103-dig_the-data](103-dig_the-data)| A Bash script that groups visitors by IP and HTTP status code, and displays this data. Uses [102-lets_parse_apache_logs](102-lets_parse_apache_logs).|
