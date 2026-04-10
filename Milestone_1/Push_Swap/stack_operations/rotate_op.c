#include "../push_swap.h"

static void	rotate_cmd(t_list **stack)
{
	t_list	*first;
	t_list	*last;

	if (!stack || !(*stack)->next)
		return ;
	first = *stack;
	*stack = (*stack)->next;
	last = ft_lstlast(*stack);
	last->next = first;
	first->next = NULL;
}

void	ra(t_list **a)
{
	rotate_cmd(a);
	ft_printf("ra\n");
}

void	rb(t_list **b)
{
	rotate_cmd(b);
	ft_printf("rb\n");
}

void	rr(t_list **a, t_list **b)
{
	rotate_cmd(a);
	rotate_cmd(b);
	ft_printf("rr\n");
}