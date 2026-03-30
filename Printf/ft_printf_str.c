#include "ft_printf.h"

/*
** Prints a null-terminated string to stdout and returns its length.
**
** Parameters:
** s : null-terminated string to print
**
** Returns:
** Number of characters written to stdout.
**
** Note:
** - If s is NULL, writes the literal string "(null)" to stdout
*/
int	ft_printf_str(char *s)
{
	int	len;

	if (s == NULL)
	{
		ft_putstr_fd("(null)", 1);
		return (ft_strlen("(null)"));
	}
	len = ft_strlen(s);
	ft_putstr_fd(s, 1);
	return (len);
}
