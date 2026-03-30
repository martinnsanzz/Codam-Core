#include "ft_printf.h"

static char	*str_malloc(int base_size, unsigned int num, int	*len);
static int	print_hex(const char *base, unsigned int num, int *len);

/*
** Prints an integer as a hexadecimal string to stdout.
**
** Parameters:
** num  : signed integer to convert; if negative, reinterpreted as unsigned
**        via implicit cast to match printf's %x/%X behavior
** conv : format specifier — 'x' for lowercase, 'X' for uppercase hex
**
** Returns:
** Number of characters written to stdout.
**
** Behavior:
** - Selects lowercase base "0123456789abcdef" for 'x'
** - Selects uppercase base "0123456789ABCDEF" for 'X'
** - Delegates conversion and output to print_hex
**
** Note:
** Negative values are reinterpreted as their unsigned equivalent,
** matching printf's %x/%X behavior: e.g. -1 prints as "ffffffff".
*/
int	ft_printf_hex(int num, char conv)
{
	int			len;
	const char	*lower_base;
	const char	*upper_base;

	len = 1;
	lower_base = "0123456789abcdef";
	upper_base = "0123456789ABCDEF";
	if (conv == 'x')
		if (!print_hex(lower_base, num, &len))
			return (0);
	else if (conv == 'X')
		if (!print_hex(upper_base, num, &len))
			return (0);
	return (len);
}

/*
** Converts an integer to a hex string using the given base and prints it.
**
** Parameters:
** base : null-terminated base string (16 characters, lower or uppercase)
** num  : value to convert, passed as unsigned int
** len  : pointer to digit count initialized by caller; updated by str_malloc
**
** Returns:
** 1 if everything worked accordingly
** 0 if allocation fails
**
** Behavior:
** - Assigns num to u_num as unsigned int; negative values wrap to their
**   unsigned equivalent via implicit reinterpretation
** - Allocates a buffer via str_malloc sized for the full hex representation
** - Fills the buffer right-to-left using modulo 16 and integer division
*/
static int	print_hex(const char *base, unsigned int num, int *len)
{
	unsigned int u_num;
	int		i;
	char	*str;

	u_num = num;
	str = str_malloc(ft_strlen(base), u_num, len);
	if (str == NULL)
		return (0);
	i = *len;
	while (i > 0)
	{
		str[i - 1] = base[num % 16];
		num /= 16;
		i--;
	}
	ft_putstr_fd(str, 1);
	free(str);
	return (1);
}

/*
** Allocates a zero-initialized buffer sized to hold the hex representation of num.
**
** Parameters:
** base_size : size of the base (16 for hexadecimal)
** num       : unsigned integer whose digit count determines allocation size
** len       : pointer to digit counter; incremented once per extra digit beyond first
**
** Returns:
** Pointer to an allocated, zero-initialized char buffer.
** NULL if ft_calloc fails.
*/
static char	*str_malloc(int base_size, unsigned int num, int	*len)
{
	char	*str;

	while (num >= base_size)
	{
		num = num / base_size;
		*len += 1;
	}
	str = ft_calloc(*len + 1, sizeof(char));
	if (str == NULL)
		return (NULL);
	return (str);
}
