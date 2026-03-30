#include "../../ft_printf.h"
#include <stdio.h>
#include <limits.h>

int	main(void)
{
	int	a = 0;
	int b = 0;
	char	*str = NULL;

	a = ft_printf("%x\n", -2147483648 );
	b = printf("%x\n", -2147483648 );
	printf("a: %d; b: %d\n", a, b);
	//printf("b: %d\n", b);
	return (0);
}