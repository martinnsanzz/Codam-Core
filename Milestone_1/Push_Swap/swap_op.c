#include "push_swap.h"

static void	swap_cmd(t_list **stack)
{
	int	temp;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	temp = *(int *)(*stack)->content;
	*(int *)(*stack)->content = *(int *)(*stack)->next->content;
	*(int *)(*stack)->next->content = temp;
}

void	sa(t_list **a)
{
	swap_cmd(a);
	ft_printf("sa\n");
}

void	sb(t_list **b)
{
	swap_cmd(b);
	ft_printf("sb\n");
}

void	ss(t_list **a, t_list **b)
{
	swap_cmd(a);
	swap_cmd(b);
	ft_printf("ss\n");
}