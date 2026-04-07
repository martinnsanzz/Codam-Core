#include "push_swap.h"

long	ft_atoi_strict(const char *nptr)
{
	int		sign;
	long	num;

	sign = 1;
	num = 0;
	while (*nptr == ' ' || (*nptr >= 9 && *nptr <= 13))
		nptr++;
	if (*nptr == '+' || *nptr == '-')
	{
		if (*nptr == '-')
			sign *= -1;
		nptr++;
	}
	if (!ft_isdigit(*nptr))
			print_error();
	while (*nptr >= '0' && *nptr <= '9')
	{
		num = num * 10 + (*nptr - '0');
		nptr++;
	}
	if (*nptr != '\0')
		print_error();
	return (num * sign);
}

void print_error()
{
	ft_putstr_fd("Error\n", 2);
	exit (1);
}