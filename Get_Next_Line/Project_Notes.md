# Get Next Line Behaviour

*Main Logic*
1. Open file to get file descriptor
	- Null if open failed
2. Enter loop (as many lines I want to print)
3. Call get_next_line (Get a new line each time is called)
4. Close file

*Get_Next_Line Logic*
Variables:
- static char *buffer -> Stores bytes from the file as char values

- char *result -> Copied string from buffer up until '\n' or '\0'. 
This is the value returned (The line)

- char *tmp -> Stores buffer while its getting joined to free it safely

- char *tmp_buffer -> Stores the string so it can be joined to
buffer and free after

- ssize_t bytes -> The return value of read(), it tells how many bytes
were actually read and points out the end-of-file when is 0, or if 
an error ocurred if -1

Behaviour:
1. Set result to NULL (Start clean every call)
2. Set bytes to 1 on start (Which makes condition TRUE on 
while loop)
3. Check if buffer is NULL (This means first call since static
variables if no value given when init the get set to NULL)
	- If buffer == NULL -> buffer = ft_calloc(1, 1) which is an
	empty string
	- If not empty check if it has '\n' or '\0'
		- If YES, skip read()
		- If NO;
4. Allocate tmp_buffer ```ft_calloc(BUFFER_SIZE + 1, sizeof(char))```
*Enter While Loop*
- While loop condition (!ft_strchr(buffer, '\n') && bytes > 0) 

tmp_buffer gets set to zero every iteration
Every iteration, buffer needs to be updated and join with the new information
This new string is stored temporarily inside tmp_buffer
Old buffer needs to be freed everytime join is called
```c
while (!ft_strchr(buffer, '\n') && bytes > 0)
	tmp = buffer;
	ft_bzero(tmp_buffer, BUFFER_SIZE + 1);
	bytes = read(fd, tmp_buffer, BUFFER_SIZE);
	buffer = ft_strjoin(tmp, tmp_buffer);
	free(tmp);
free(tmp_buffer);
```

3. Once '\n' or EOF is found extract_line()
*extract_line()*
This function splits the buffer from the beggining until '\n' and returns the line.
It also allocates dinamically the amount of memory needed for result

5. Remove the line to the buffer (Including '\n'), trim_buffer()
*trim_buffer()*
This functions move the pointer until '\n' (including) and returns that pointer shifted

Since we are shifting a pointer the original allocation still exits and needs to be freed.
```c
tmp = buffer;
buffer = trim_buffer();
free(tmp)
````

6. Return result

Returns:
- New line '\n' terminated
- Last line '\0' if bytes is 0 (End of file) but buffer is not empty
- NULL if bytes is 0 and buffer is empty (No more text) or if error
ocurred