#include "../push_swap.h"

void	complex_strat(t_list **stack_a, t_list **stack_b,
				t_operations *op, t_flags *flags)
{
	(void)stack_b;
	(void)stack_a;
	(void)op;
	flags->strategy = COMPLEX;
	//print_stack(*stack_a, "stack_a");
	ft_printf("Inside complex strat\n");
}
