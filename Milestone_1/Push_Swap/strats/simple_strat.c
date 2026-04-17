#include "../push_swap.h"

void	simple_strat(t_list **stack_a, t_list **stack_b,
				t_operations *op, t_flags *flags)
{
	int	min_pos_index;
	int	stack_size;

	set_flags(flags, SIMPLE);
	while (*stack_a != NULL)
	{
		stack_size = ft_lstsize(*stack_a);
		min_pos_index = find_min(*stack_a);
		if (min_pos_index < stack_size / 2)
			while (min_pos_index--)
				ra(stack_a, op, flags->bench);
		else if (min_pos_index != 0)
		{
			min_pos_index = stack_size - min_pos_index;
			while (min_pos_index--)
				rra(stack_a, op, flags->bench);
		}
		pb(stack_b, stack_a, op, flags->bench);
	}
	while (*stack_b != NULL)
		pa(stack_a, stack_b, op, flags->bench);
}

int	find_min(t_list	*stack)
{
	t_list	*min_node;
	int		node_pos;
	int		min_pos_index;

	node_pos = 0;
	min_pos_index = 0;
	min_node = stack;
	while (stack != NULL)
	{
		if (*(int *)stack->content < *(int *)min_node->content)
		{
			min_node = stack;
			min_pos_index = node_pos;
		}
		node_pos += 1;
		stack = stack->next;
	}
	return (min_pos_index);
}
