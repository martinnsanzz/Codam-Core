#include "../push_swap.h"
#include <stdio.h>

static bool	find_node(t_list *stack, int *index, int cur_chunk, int chunk_size);
static void	rotate_to_top(t_list **stack, int node_index,
				t_operations *op, bool bench);
static void	push_sorted_to_a(t_list **stack_b, t_list **stack_a,
				t_operations *op, bool bench);

void	medium_strat(t_list **stack_a, t_list **stack_b,
			t_operations *op, t_flags *flags)
{
	int	total_chunks;
	int	chunk_size;
	int	stack_size;
	int	curr_chunk;
	int	node_index;

	flags->strategy = MEDIUM;
	stack_size = ft_lstsize(*stack_a);
	total_chunks = ft_sqrt(stack_size);
	chunk_size = (stack_size + total_chunks - 1) / total_chunks;
	curr_chunk = 0;
	while (curr_chunk < total_chunks)
	{
		node_index = 0;
		while (find_node(*stack_a, &node_index, curr_chunk, chunk_size))
		{
			rotate_to_top(stack_a, node_index, op, flags->bench);
			pb(stack_b, stack_a, op, flags->bench);
		}
		curr_chunk++;
	}
	push_sorted_to_a(stack_b, stack_a, op, flags->bench);
}

static bool	find_node(t_list *stack, int *index, int cur_chunk, int chunk_size)
{
	int	node_pos;

	node_pos = 0;
	while (stack != NULL)
	{
		if ((*(int *)stack->content) / chunk_size == cur_chunk)
		{
			*index = node_pos;
			return (true);
		}
		node_pos += 1;
		stack = stack->next;
	}
	return (false);
}

static void	rotate_to_top(t_list **stack, int node_index,
				t_operations *op, bool bench)
{
	int	cur_size;

	cur_size = ft_lstsize(*stack);
	if (node_index < cur_size / 2)
		while (node_index--)
			ra(stack, op, bench);
	else if (node_index != 0)
		while (node_index++ != cur_size)
			rra(stack, op, bench);
}

static void	push_sorted_to_a(t_list **stack_b, t_list **stack_a,
					t_operations *op, bool bench)
{
	int	stack_size;
	int	max_pos;
	int	restore;

	stack_size = ft_lstsize(*stack_b);
	while (stack_size--)
	{
		max_pos = find_max(*stack_b);
		restore = max_pos;
		if (max_pos != 0)
			while (max_pos--)
				rb(stack_b, op, bench);
		pa(stack_a, stack_b, op, bench);
		while (restore--)
			rrb (stack_b, op, bench);
	}
}

int	find_max(t_list	*stack)
{
	t_list	*max_node;
	int		node_pos;
	int		max_pos_index;
	int		i;

	node_pos = 0;
	max_pos_index = 0;
	max_node = stack;
	i = 0;
	while (stack != NULL)
	{
		if (*(int *)stack->content > *(int *)max_node->content)
		{
			max_node = stack;
			max_pos_index = node_pos;
		}
		node_pos += 1;
		stack = stack->next;
		i++;
	}
	return (max_pos_index);
}
