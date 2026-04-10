#include "push_swap.h"

static void	init_flags(t_flags *flags);

int	main(int argc, char *argv[])
{
	t_flags	flags;
	t_list	*link_lst;
	int		*tmp_lst;
	int		n_elements;

	init_flags(&flags);
	n_elements = check_argv(argc, argv, &tmp_lst, &flags);
	// print_flags(flags);
	// print_lst(tmp_lst, n_elements, "Unsorted list:");
	if (!tmp_lst || argc < (3 + flags.n_flags))
		return (0);
	normalize(&tmp_lst, n_elements);
	// print_lst(tmp_lst, n_elements, "Normalized list:");
	linked_lst_creation(&link_lst, tmp_lst, n_elements);
	print_link_lst(link_lst);
	ft_lstclear(&link_lst, (*free));
	free(tmp_lst);
	return (0);
}

/**
 * @brief Initializes flags to default states:
 * 			- Number of flags = 0
 * 			- Bench mode = 0 (False / Off)
 * 			- Strategy = Adaptive / 0
 */
static void	init_flags(t_flags *flags)
{
	flags->n_flags = 0;
	flags->bench = 0;
	flags->strategy = ADAPTIVE;
}
