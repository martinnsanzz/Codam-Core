#include <stdio.h>
#include "../attempt_1/libft.h"

//gcc -Wall -Wextra -Werror test_ft_isprint.c ../attempt_1/ft_isprint.c

int	main(void)
{
	printf("' ' -> %d (expected 1)\n", ft_isprint(' '));
	printf("'~' -> %d (expected 1)\n", ft_isprint('~'));
	printf("'A' -> %d (expected 1)\n", ft_isprint('A'));

	printf("31 -> %d (expected 0)\n", ft_isprint(31));
	printf("127 -> %d (expected 0)\n", ft_isprint(127));
	printf("\\n -> %d (expected 0)\n", ft_isprint('\n'));

	return (0);
}