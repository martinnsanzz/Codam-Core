#include "../../ft_printf.h"
#include <stdio.h>

int	main(void)
{
	int	a = 0;
	int b = 0;

	a = ft_printf("hello %%\n");
	b = printf("hello %%\n");
	printf("a: %d; b: %d\n", a, b);
	return (0);
}