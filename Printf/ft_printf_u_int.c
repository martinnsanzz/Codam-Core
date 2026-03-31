#include "ft_printf.h"

static	void	digit_counter(unsigned int num, int *len);

/**
 * @brief  Recursively prints an unsigned integer to stdout and returns its digit count.
 *
 * @details  Counts total digits via digit_counter, then recurses on num / 10 to
 *           print most-significant digits first, writing each digit character
 *           individually via write(1).
 *
 * @param  num  unsigned int — The value to print. Negative int values passed at
 *                             the call site are implicitly converted to unsigned,
 *                             wrapping to UINT_MAX range before this function runs.
 *
 * @return int — The number of decimal digits written to stdout.
 *               Always >= 1 (a value of 0 produces one digit: "0").
 */
void	ft_printf_u_int(unsigned int num, int *len)
{
	unsigned int	nb;
	char			c;

	nb = num;
	if (num < 0)
		nb = UINT_MAX - (nb * -1);
	digit_counter(nb, len);
	if (nb >= 10)
		ft_printf_u_int(nb / 10, len);
	c = (nb % 10) + '0';
	write (1, &c, 1);
}

static	void	digit_counter(unsigned int num, int *len)
{
	while (num >= 10)
	{
		num /= 10;
		len++;
	}
	*len += 1;
}
