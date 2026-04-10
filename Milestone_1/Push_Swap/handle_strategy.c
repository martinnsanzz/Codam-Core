#include "push_swap.h"

static float compute_disorder(t_list *stack);

void	select_strategy(t_list **stack, t_flags flags, int n_elements)
{
	
}

static float compute_disorder(t_list *stack)
{
	float		mistakes;
	float		total_pairs;
	t_list		*i;
	t_list		*j;

	if (!stack)
		return (0);
	mistakes = 0;
	total_pairs = 0;
	i = stack;
	while (i->next != NULL)
	{
		j = i->next;
		while (j != NULL)
		{
			if (*(int *)i->content > *(int *)j->content)
				mistakes += 1;
			j = j->next;
			total_pairs += 1;
		}
		i = i->next;
	}
	return (mistakes / total_pairs);
}