#include "push_swap.h"

int	ft_sqrt(int nb)
{
	float	res;
	int		odd;

	odd = 1;
	res = 0;
	if (nb < 0)
		return (res);
	while (odd <= nb)
	{
		if (odd % 2 != 0)
		{
			nb -= odd;
			res++;
		}
		odd++;
	}
	if (nb != 0)
		return (res + 1);
	return (res);
}
