#include "../push_swap.h"

static int	max_bits(t_list *stack);

void	complex_strat(t_list **stack_a, t_list **stack_b,
				t_operations *op, t_flags *flags)
{
	int stack_size;
	int restore;
	int	i;
	int	bits;


	set_flags(flags, COMPLEX);
	bits = max_bits(*stack_a);
	ft_printf("\n\nMaximum bits [%d]\n\n", bits);
	// ft_printf("\nBefore sort\n");
	// print_stack_int_base(*stack_a, "Stack A", "01");
	// print_stack_int_base(*stack_b, "Stack B", "01");
	i = 0;
	while (i < bits)
	{
		stack_size = ft_lstsize(*stack_a);
		while (stack_size > 0)
		{
			if (((*(int *)(*stack_a)->content >> i) & 1) == 0)
				pb(stack_b, stack_a, op, flags->bench);
			else
				ra(stack_a, op, flags->bench);
			stack_size--;
		}
		ft_printf("Bit [%d]\n", i);
		print_stack_int_base(*stack_a, "Stack A", "01");
		print_stack_int_base(*stack_b, "Stack B", "01");
		restore = ft_lstsize(*stack_b);
		while (restore--)
			pa(stack_a, stack_b, op, flags->bench);
		i++;
	}
	ft_printf("After sort\n");
	print_stack_int_base(*stack_a, "Stack A", "01");
	print_stack_int_base(*stack_b, "Stack B", "01");
}

static int	max_bits(t_list *stack)
{
	int	stack_size;
	int	max_value;
	int	bits;

	stack_size = ft_lstsize(stack);
	max_value = stack_size - 1;
	bits = 0;
	while (max_value)
	{
		bits++;
		max_value >>= 1;
	}
	return (bits);
}
