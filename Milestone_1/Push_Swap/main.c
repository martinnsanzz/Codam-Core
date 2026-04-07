#include "push_swap.h"

int	main(int argc, char *argv[])
{
	int	is_flag;

	if (argc < 2)
		return (0);
	is_flag = 0;
	check_argv(argc, argv, &is_flag);
	ft_printf("Is flag value: %d\n", is_flag);
	ft_putstr_fd("In main\n", 1);
	return (0);
}