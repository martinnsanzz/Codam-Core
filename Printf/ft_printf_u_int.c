#include "ft_printf.h"

static	int	digit_counter(unsigned int num);

/*
** Recursively prints an unsigned integer to stdout and returns its digit count.
**
** Parameters:
** num : unsigned integer to print
**
** Returns:
** Number of characters written (digit count of num).
**
** Note:
** - If the original value was negative, reinterprets it as UINT_MAX - (val * -1)
**   to match printf's %u behavior for negative signed integers
*/
int	ft_printf_u_int(unsigned int num)
{
	unsigned int	nb;
	int				len;
	char			c;

	nb = num;
	if (num < 0)
		nb = UINT_MAX - (nb * -1);
	len = digit_counter(nb);
	if (nb >= 10)
		ft_printf_u_int(nb / 10);
	c = (nb % 10) + '0';
	write (1, &c, 1);
	return (len);
}


static	int	digit_counter(unsigned int num)
{
	int	len;

	len = 0;
	while (num >= 10)
	{
		num /= 10;
		len++;
	}
	len++;
	return (len);
}
