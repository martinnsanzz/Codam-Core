#include "push_swap.h"

static void	init_flags(t_flags *flags);

int	main(int argc, char *argv[])
{
	t_flags	flags;
	int		*lst;
	int		n_elements;

	init_flags(&flags);
	n_elements = check_argv(argc, argv, &lst, &flags);
	//print_flags(flags);
	//print_lst(lst, n_elements, "Unsorted list:");
	if (!lst || argc < (3 + flags.n_flags))
		return (0);
	normalize(&lst, n_elements);
	//print_lst(lst, n_elements, "Normalized list:");
	free(lst);
	return (0);
}

static void	init_flags(t_flags *flags)
{
	flags->n_flags = 0;
	flags->bench = 0;
	flags->strategy = ADAPTIVE;
}
