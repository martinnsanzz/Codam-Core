#include "ft_printf.h"

int ft_printf_ptr(void *p)
{
	(void)p;
	ft_putstr_fd("Inside print_ptr\n", 1);
	return (0);
}
