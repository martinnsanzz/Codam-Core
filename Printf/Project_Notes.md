The main mechanic of *ft_printf* project is the use of `Variadic Functions`.
They allow functions to accept an arbitrary number of arguments with
the use of ellipsis `(...)` as one of the arguements

```c
int	ft_printf(const char *format, ...);
```
>The arguments passed to the function using `ellipsis` are called variable
>arguement (va)

# Allowed Functions
1. `va_list` is a way for C functions to accept a variable number of arguments. 
It's like a special kind of list that holds all the extra arguments you pass 
to a function.
2. `va_start`: Think of this as "starting the list". It initialises the list to 
point to the first variable argument.
3. `va_arg`: This is how you get the next argument from the list.
4. `va_end`: This "ends the list" and cleans things up.
5. `va_copy`: This is for copying the list.

>All these functions are found in the `stdarg.h` library.

```c
va_list ap;
va_start(ap, last_named_param);
// call va_arg as many times as needed
va_end(ap);
```

# ft_printf behaviour
1. Set up va_list and initialize the list to the first arguement past `str``
2. Loop throught the string in a while loop and look for `%`char
3. If found check the next character and act accordingly:
	- %c Prints a single character.
	- %s Prints a string (as defined by the common C convention).
	- %p The void * pointer argument has to be printed in hexadecimal format.
	- %d Prints a decimal (base 10) number.
	- %i Prints an integer in base 10.
	- %u Prints an unsigned decimal (base 10) number.
	- %x Prints a number in hexadecimal (base 16) lowercase format.
	- %X Prints a number in hexadecimal (base 16) uppercase format.
	- %% Prints a percent sign.
>Depending on the format specifier called the required function (e.g., if %s; 
>call ft_putstr_fd from libft)
4. After reaching the end of the string clean the memory of va_list

*RETURN*
On success - The number of characters printed
On failure - A negative number (-1)

To keep track of the amount of character printed all functions created for 
printing each format specifier will return `int` which will be the amount of 
characters printed and this value will keep adding until the end of ft_printf

*Files for the format specifiers*


- **ft_prinf_char.c** - This file will contain a function that will:
1. Check the format specifier (%c or %%)
2. Print the character passed (`%`if its %%)
3. Return (1);

```c
int ft_printf_char(char c);
```

- **ft_printf_hex.c** - This file will contain a fucntion that will: 
1. Check the format specifier (%x or %X)
2. Convert the integer in decimal base to hexadecimal base
3. Print each character
4. Return the length of the number in hex

```c
int	ft_printf_hex(int num, char conv);
```

- **ft_printf_int.c** - This file will contain a function that will:
1. Check the format specifier (%d, %i or %u)
2. Print the number passed adhering to the format specifier
   (e.g., if %u and number passed is - value, it will make it positive)
3. Return the length of the number printed

```c
int	ft_printf_int(int num, char conv);
```

- **ft_printf_ptr.c** - This file will contain a function that will:
2. Print the memory address of that pointer (Need to figure out how)
3. Return the length of the memory address

```c
int ft_printf_ptr(void *p);
```

- **ft_printf_str.c** - This file will contain a function that will:
1. Print the string (%s)
2. Return the length of the string

```c
int	ft_printf_str(char *s);
```
