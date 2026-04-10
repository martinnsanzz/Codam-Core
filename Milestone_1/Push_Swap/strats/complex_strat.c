#include "../push_swap.h"

void	complex_strat(t_list **stack_a, t_list **stack_b, int bench)
{
	(void)stack_b;
	print_stack(*stack_a);
	ft_printf("Bench mode [%d]\n", bench);
	ft_printf("Inside complex strat\n");
}