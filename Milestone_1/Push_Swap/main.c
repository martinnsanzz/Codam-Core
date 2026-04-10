#include "push_swap.h"

static void	init_flags(t_flags *flags);

int	main(int argc, char *argv[])
{
	t_flags	flags;
	t_list	*stack_a;
	t_list	*stack_b;
	int		*tmp_lst;
	int		n_elements;

	init_flags(&flags);
	stack_b = NULL;
	n_elements = check_argv(argc, argv, &tmp_lst, &flags);
	// print_flags(flags);
	// print_lst(tmp_lst, n_elements, "Unsorted list:");
	if (!tmp_lst || argc < (3 + flags.n_flags))
		return (0);
	normalize(&tmp_lst, n_elements);
	// print_lst(tmp_lst, n_elements, "Normalized list:");
	linked_lst_creation(&stack_a, tmp_lst, n_elements);
	//print_stack(stack_a);
	select_strategy(&stack_a, &stack_b, flags);
	ft_lstclear(&stack_a, (*free));
	ft_lstclear(&stack_b, (*free));
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
