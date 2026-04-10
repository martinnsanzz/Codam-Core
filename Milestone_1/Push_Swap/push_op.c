#include "push_swap.h"

static void	push_cmd(t_list **src, t_list **dst)
{
	t_list	*temp;

	if (!src || !*src)
		return ;
	temp = *src;
	*src = (*src)->next;
	temp->next = *dst;
	*dst = temp;
}

void	pa(t_list **a, t_list **b)
{
	push_cmd(b, a);
	ft_printf("pa\n");
}

void	pb(t_list **b, t_list **a)
{
	push_cmd(a, b);
	ft_printf("pb\n");
}