#include "push_swap.h"

static void	rev_rotate_cmd(t_list **stack)
{
	t_list	*last;
	t_list	*sec_last;

	if (!stack || !(*stack)->next)
		return ;
	last = ft_lstlast(*stack);
	sec_last = *stack;
	while (sec_last->next != last)
		sec_last = sec_last->next;
	last->next = (*stack);
	sec_last->next = NULL;
	*stack = last;
}

void	rra(t_list **a)
{
	rev_rotate_cmd(a);
	ft_printf("rra\n");
}

void	rrb(t_list **b)
{
	rev_rotate_cmd(b);
	ft_printf("rrb\n");
}

void	rrr(t_list **a, t_list **b)
{
	rev_rotate_cmd(a);
	rev_rotate_cmd(b);
	ft_printf("rrr\n");
}