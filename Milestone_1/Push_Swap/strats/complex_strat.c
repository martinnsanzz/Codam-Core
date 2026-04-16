#include "../push_swap.h"

void	complex_strat(t_list **stack_a, t_list **stack_b,
				t_operations *op, t_flags *flags)
{
	int stack_size;
	int	max_value;
	int restore;
	//int	bit;

	stack_size = ft_lstsize(*stack_a);
	ft_printf("Stack_size: %d\n", stack_size);
	max_value = stack_size - 1;
	restore = 0;
	//bit = 0;
	ft_printf("\nBefore sort\n");
	print_stack(*stack_a, "Stack A");
	print_stack(*stack_b, "Stack B");
	while (stack_size > 0)
	{
		if (((*(int *)(*stack_a)->content >> 0) & 1) == 1)
		{
			restore++;
			pb(stack_b, stack_a, op, flags->bench);
		}
		ra(stack_a, op, flags->bench);
		max_value >>= 1;
		stack_size--;
		//bit++;
	}
	print_stack(*stack_b, "Stack B");
	while (restore--)
		pa(stack_a, stack_b, op, flags->bench);
	ft_printf("\nAfter sort\n");
	print_stack(*stack_a, "Stack A");
	print_stack(*stack_b, "Stack B");
}
