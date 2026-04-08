#include "push_swap.h"
#include <stdio.h>

int	main(int argc, char *argv[])
{
	t_flags flags;
	int		*unsorted_lst;

	flags.n_flags = 0;
	flags.bench = 0;
	flags.strategy = ADAPTIVE;
	unsorted_lst = NULL;
	check_argv(argc, argv, &unsorted_lst, &flags);
	if (!unsorted_lst || argc < (3 + flags.n_flags))
		return (0);
    for (int i = 0; i < (argc -1 - flags.n_flags); i++) {
        printf("%d ", unsorted_lst[i]);
    }
	free(unsorted_lst);
	return (0);
}
