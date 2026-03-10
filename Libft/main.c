
#include "attempt_1/libft.h"
#include <stdio.h>

int	main(void)
{
	const char	*str = "Hello";

	printf("Size of %s is: %zu\n", str, ft_strlen(&str[0]));
	return (0);
}
