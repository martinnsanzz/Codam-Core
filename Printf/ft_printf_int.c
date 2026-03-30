#include "ft_printf.h"

/*
** Prints a signed integer to stdout and returns the number of characters written.
**
** Parameters:
** num : signed integer to print
**
** Returns:
** Number of characters written to stdout, including the '-' sign if negative.
**
** Behavior:
** - Converts num to its string representation via ft_itoa to get the length
*/
int	ft_printf_int(int num)
{
	int		len;
	char	*s_num;

	s_num = ft_itoa(num);
	len = ft_strlen(s_num);
	ft_putnbr_fd(num, 1);
	free(s_num);
	return (len);
}
