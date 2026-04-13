#include "push_swap.h"

int	ft_sqrt(int nb)
{
	float	res;
	int		odd;

	odd = 1;
	res = 0;
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
		return (0);
	return (res);
}