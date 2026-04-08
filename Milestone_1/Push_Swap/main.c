#include "push_swap.h"

int	main(int argc, char *argv[])
{
	t_flags flags;

	flags.n_flags = 0;
	flags.bench = 0;
	flags.strategy = ADAPTIVE;
	check_argv(argc, argv, &flags);
	if (argc < (3 + flags.n_flags))
		return (0);
	return (0);
}
