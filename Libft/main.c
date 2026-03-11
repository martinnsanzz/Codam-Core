
#include "attempt_1/libft.h"
#include <stdio.h>
#include <string.h>

int	main(void)
{
	char	str[7] = "Hello";

	ft_bzero(&str[3], 1);
	for (size_t i = 0; i < 7; i++)
	{
		printf("%c ", str[i]);
	}
	printf("\n");
	return (0);
}
