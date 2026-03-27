#include "ft_printf.h"

int	ft_printf_char(char c)
{
	ft_putchar_fd(c, 1);
	return (1);
}
