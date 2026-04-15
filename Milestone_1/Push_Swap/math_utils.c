#include "push_swap.h"

/**
 * @brief  Computes the ceiling integer square root of a non-negative integer.
 *
 * @details  Uses the property that the sum of the first n odd numbers equals n².
 *           Repeatedly subtracts successive odd numbers from `nb`, incrementing
 *           the root counter each time. If `nb` reaches exactly 0, the input was
 *           a perfect square and `res` is returned directly. If the loop exits
 *           with `nb > 0`, the input was not a perfect square and `res + 1` is
 *           returned as the ceiling.
 *
 * @return int — Ceiling of sqrt(nb). Returns 0 for negative input or 0.
 */
int	ft_sqrt(int nb)
{
	int	res;
	int	odd;

	odd = 1;
	res = 0;
	if (nb <= 0)
		return (res);
	while (odd <= nb)
	{
		nb -= odd;
		res++;
		odd += 2;
	}
	if (nb != 0)
		return (res + 1);
	return (res);
}
