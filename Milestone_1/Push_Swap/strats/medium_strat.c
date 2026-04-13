#include "../push_swap.h"

void	medium_strat(t_list **stack_a, t_list **stack_b,
				t_operations *op, t_flags *flags)
{
	(void)stack_b;
	(void)op;
	flags->strategy = MEDIUM;
	print_stack(*stack_a, "stack_a");
	ft_printf("Inside medium strat\n");
}
