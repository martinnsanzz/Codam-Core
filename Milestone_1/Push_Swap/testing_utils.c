#include "push_swap.h"
#include <stdio.h>

void	print_link_lst(t_list *lst)
{
	int		i;

	i = 0;
	while (lst != NULL)
	{
		printf("Node: %d -> Content [%d]\n", i, *(int *)lst->content);
		lst = lst->next;
		i++;
	}
}

void	print_lst(int *lst, int n_elements, char *msg)
{
	size_t	i;

	i = 0;
	ft_printf("%s\n", msg);
	while (i < (size_t)n_elements)
		ft_printf("[%d] ", lst[i++]);
	ft_printf("\n\n");
}

void	print_flags(t_flags flags)
{
	ft_printf("==== FLAGS ====\n");
	ft_printf("Number of flags: %d\n", flags.n_flags);
	ft_printf("Strategy: %d\n", flags.strategy);
	ft_printf("Bench mode: %d\n", flags.bench);
	ft_printf("===============\n");
	ft_printf("\n\n");
}
