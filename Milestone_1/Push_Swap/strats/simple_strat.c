#include "../push_swap.h"

static int	find_min(t_list	*stack);

void	simple_strat(t_list **stack_a, t_list **stack_b, int bench)
{
	int	min_pos_index;
	int	stack_size;

	(void)bench;
	while (*stack_a != NULL)
	{
		stack_size = ft_lstsize(*stack_a);
		min_pos_index = find_min(*stack_a);
		if (min_pos_index == 0)
		{
			pb(stack_a, stack_b);
			continue;
		}
		if (min_pos_index < stack_size / 2)
			while (min_pos_index--)
				ra(stack_a);
		else
		{
			min_pos_index = stack_size - min_pos_index;
			while (min_pos_index--)
				rra(stack_a);
		}
		pb(stack_a, stack_b);
	}
	while (*stack_b != NULL)
		pa(stack_a, stack_b);
}

static int	find_min(t_list	*stack)
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
