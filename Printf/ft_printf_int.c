#include "ft_printf.h"

int	ft_printf_int(int num, char conv)
{
	(void)num;
	(void)conv;
	ft_putstr_fd("Inside print_int\n", 1);
	return (0);
}
