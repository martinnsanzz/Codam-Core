#include "ft_printf.h"

static int	ft_handle_spec(char c, va_list args);
static int	check_format(const char	c);

/*
** Parses a format string and writes formatted output to stdout.
**
** Parameters:
** format : null-terminated format string containing text and format specifiers
** ...    : variadic arguments matching each format specifier in order
**
** Returns:
** Total number of characters written to stdout.
**
** Behavior:
** - Iterates over each character in the format string
** - On '%', reads the next character as a format specifier and consumes
**   one variadic argument via va_arg(args, void *)
** - On any other character, writes it directly to stdout via ft_putchar_fd
** - Accumulates the character count returned by each handler
*/
int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		len;

	va_start(args, format);
	len = 0;
	while (*format != '\0')
	{
		if (*format == '%')
		{
			if (!check_format(*(format + 1)))
				ft_putchar_fd(*format, 1);
			else
				len += ft_handle_spec(*(format + 1), args);
			format++;
		}
		else 
		{
			ft_putchar_fd(*format, 1);
			len++;
		}
		format++;
	}
	va_end(args);
	return (len);
}

/*
** Dispatches a single format specifier to the appropriate print handler.
**
** Parameters:
** c   : the format specifier character (e.g. 'c', 's', 'd', 'x', 'X',
**       'u', 'i', 'p', '%')
** arg : the variadic argument passed as void *, cast internally per specifier
**
** Returns:
** Number of characters written to stdout for this specifier.
** 0 if the specifier is unrecognized.
**
** Behavior:
** - '%%' : writes a literal '%' and returns 1
** - 'c'  : casts arg to char, delegates to ft_printf_char
** - 'x'/'X' : casts arg to int, delegates to ft_printf_hex with case flag
** - 'd'/'i'/'u' : casts arg to int, delegates to ft_printf_int
** - 'p'  : passes arg as void *, delegates to ft_printf_ptr
** - 's'  : casts arg to char *, delegates to ft_printf_str
**
*/
static int	ft_handle_spec(char c, va_list args)
{
	int	len;

	len = 0;
	if (c == '%')
	{
		ft_putchar_fd('%', 1);
		len++;
	}
	else if (c == 'c')
	{
		ft_putchar_fd(va_arg(args, int), 1);
		len++;
	}
	else if (c == 'x' || c == 'X')
		len += ft_printf_hex(va_arg(args, unsigned int), c);
	else if (c == 'd' || c == 'i')
		len += ft_printf_int(va_arg(args, int));
	else if (c == 'u')
		len += ft_printf_u_int(va_arg(args, unsigned int));
	else if (c == 'p')
		len += ft_printf_ptr(va_arg(args, void *));
	else if (c == 's')
		len += ft_printf_str(va_arg(args, char *));
	return (len);
}

/*
** Checks if the format specifier is correct and within the list
**
** Parameters:
** c	: Character to check
**
** Returns:
** 1 if its correct
** 0 if its not correct
*/
static int	check_format(const char	c)
{
	if (c == '%' 
		|| c == 'c'
		|| c == 'x'
		|| c == 'X'
		|| c == 'd'
		|| c == 'u'
		|| c == 'i'
		|| c == 'p'
		|| c == 's')
		return (1);
	return (0);
}
