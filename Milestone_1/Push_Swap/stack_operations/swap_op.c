#include "../push_swap.h"

static void	swap_cmd(t_list **stack)
{
	int	temp;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	temp = *(int *)(*stack)->content;
	*(int *)(*stack)->content = *(int *)(*stack)->next->content;
	*(int *)(*stack)->next->content = temp;
}

/**
 * @brief Swap the first two elements at the top of stack a. 
 * 		  Do nothing if there is only one or no elements.
 */
void	sa(t_list **stack_a, t_operations *op, bool bench)
{
	swap_cmd(stack_a);
	op->sa += 1;
	if (bench == false)
		ft_printf("sa\n");
}

/**
 * @brief Swap the first two elements at the top of stack b.
 * 		  Do nothing if there is only one or no elements.
 */
void	sb(t_list **stack_b, t_operations *op, bool bench)
{
	swap_cmd(stack_b);
	op->sb += 1;
	if (bench == false)
		ft_printf("sb\n");
}

/**
 * @brief sa and sb at the same time.
 */
void	ss(t_list **stack_a, t_list **stack_b, t_operations *op, bool bench)
{
	swap_cmd(stack_a);
	swap_cmd(stack_b);
	op->ss += 1;
	if (bench == false)
		ft_printf("ss\n");
}
