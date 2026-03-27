#include "ft_printf.h"

static int	ft_handle_spec(char c, void *arg);

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
	int	len;
	int	i;
	va_list	args;

	va_start(args, format);
	len = 0;
	i = 0;
	while (format[i] != '\0')
	{
		if (format[i] == '%')
		{
			len += ft_handle_spec(format[i + 1], va_arg(args, void *));
			i++;
		}
		else
		{
			ft_putchar_fd(format[i], 1);
			len++;
		}
		i++;
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
static int	ft_handle_spec(char c, void *arg)
{
	int	len;

	len = 0;
	if (c == '%')
	{
		ft_putchar_fd('%', 1);
		len++;
	}
	else if (c == 'c')
		len += ft_printf_char((char)arg);
	else if (c == 'x' || c == 'X')
		len += ft_printf_hex((int)arg, c);
	else if (c == 'd' || c == 'u' || c == 'i')
		len += ft_printf_int((int)arg, c);
	else if (c == 'p')
		len += ft_printf_ptr(arg);
	else if (c == 's')
		len += ft_printf_str((char *)arg);
	return (len);
}
