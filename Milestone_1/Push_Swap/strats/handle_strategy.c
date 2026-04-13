#include "../push_swap.h"
#include <stdio.h>

static float	compute_disorder(t_list *stack_a);

/**
 * @brief  Selects and dispatches a sorting strategy based on flags 
 * 		   or disorder score.
 *
 * @details  If `flags.strategy` is 0 (ADAPTIVE), computes the 
 * 			 disorder score of `stack_a` and selects a strategy 
 * 			 automatically. If a strategy was explicitly
 *           set via flags, dispatches directly to the corresponding
 * 			 function without computing disorder.
 */
void	select_strategy(t_list **stack_a, t_list **stack_b, t_flags *flags)
{
	float			disorder;
	t_operations	operations;

	disorder = compute_disorder(*stack_a);
	ft_memset(&operations, 0, sizeof(t_operations));
	if (flags->strategy == ADAPTIVE)
	{
		if (disorder < 0.2)
			simple_strat(stack_a, stack_b, &operations, flags);
		else if (disorder >= 0.2 && disorder <= 0.5)
			medium_strat(stack_a, stack_b, &operations, flags);
		else
			complex_strat(stack_a, stack_b, &operations, flags);
	}
	else
	{
		if (flags->strategy == SIMPLE)
			simple_strat(stack_a, stack_b, &operations, flags);
		else if (flags->strategy == MEDIUM)
			medium_strat(stack_a, stack_b, &operations, flags);
		else if (flags->strategy == COMPLEX)
			complex_strat(stack_a, stack_b, &operations, flags);
	}
	if (flags->bench == 1)
		bench(*flags, operations, disorder);
}

/**
 * @brief  Computes the disorder ratio of a linked list of integers.
 *
 * @details  Counts all pairs (i, j) where i appears before j in the 
 * 			 list but holds a greater value. The disorder score is 
 * 			 the ratio of inversions to total pairs examined, 
 * 			 producing a value in [0.0, 1.0].
 * 
 * @return float — Inversion ratio in the range [0.0, 1.0].
 *                 0.0 indicates a fully sorted list or NULL/single-node input.
 *                 1.0 indicates a fully reversed list.
 */
static float	compute_disorder(t_list *stack_a)
{
	float		mistakes;
	float		total_pairs;
	t_list		*current;
	t_list		*next;

	if (!stack_a)
		return (0);
	mistakes = 0;
	total_pairs = 0;
	current = stack_a;
	while (current->next != NULL)
	{
		next = current->next;
		while (next != NULL)
		{
			if (*(int *)current->content > *(int *)next->content)
				mistakes += 1;
			next = next->next;
			total_pairs += 1;
		}
		current = current->next;
	}
	return (mistakes / total_pairs);
}
