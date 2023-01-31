# Command Line for A Win

- Project contains the soultion to the [cdmchallenge](https://cmdchallenge.com/#/move_file). 

## 0-first_9_tasks.PNG: Solved challenge 1 to 9. 

- Challenge 1: Your first challenge is to print "hello world" on the terminal in a single command.
```
echo 'hello world'
```
- Chellenge 2: Print the current working directory.

 ```
 pwd 
 ```

- Challenge 3: List names of all the files in the current directory, one file per line.

 ```
 ls
 ```
- Challenge 4: There is a file named access.log in the current directory. Print the contents.
```
cat access.log
```
- challenge 5: Print the last 5 lines of "access.log"
```
tail -5 5 access.log
```
- challenge 6: Create an empty file named take-the-command-challenge in the current working directory.
 ```
 touch take-the-command-challenge
 ```
- Challenge 7: Create a directory named tmp/files in the current working directory

```
mkdir tmp/ tmp/files
```
- challenge 8: Copy the file named take-the-command-challenge to the directory tmp/files
```
cp take-the-command-challenge tmp/files
```
- challenge 9: Move the file named take-the-command-challenge to the directory tmp/files
 ```
 mv take-the-command-challenge tmp/files
 ```
## 1-next_9_tasks.PNG: Solved challenge 10 to 18. 
- challenge 10: A symbolic link is a type of file that is a reference to another file. Create a symbolic link named take-the-command-challenge that points to the file tmp/files/take-the-command-challenge.
```
ln -s tmp/files/take-the-command-challenge
```
- challenge 11: Delete all of the files in this challenge directory including all subdirectories and their contents.
```
find . -delete
```
Challenge 12: 
There are files in this challenge with different file extensions. Remove all files with the .doc extension recursively in the current working directory.
```
find . type f -name *.doc -delete
```
challenge 13: There is a file named access.log in the current working directory. Print all lines in this file that contains the string "GET"
```
grep "GER" access.log
```
challenge 14: Print all files in the current directory, one per line (not the path, just the filename) that contain the string "500".
```
grep -rl "500"
```
challenge 15: Print the relative file paths, one path per line for all filenames that start with "access.log" in the current directory.

```
ls
```
or
```
ls -1 | grep "^access.log"
```
challenge 16: Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log" that contain the string "500". Note that there are no files named access.log in the current directory, you will need to search recursively

## 2-next_9_tasks.PNG: Solved challenge 18 to 27.
