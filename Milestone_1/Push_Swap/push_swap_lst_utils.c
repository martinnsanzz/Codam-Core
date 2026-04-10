#include "push_swap.h"

/**
 * @brief  Builds a linked list from a normalized integer array.
 *
 * @details  Iterates over `normalize_lst`, allocating a new `int` on the heap for
 *           each element and wrapping it in a `t_list` node via `ft_lstnew`. Each
 *           node is appended to `*link_lst` via `ft_lstadd_back`. On `ft_lstnew`
 *           failure, `ft_lstclear` is called to free the lis
 *
 * @param  link_lst       t_list** — Output parameter. Set to NULL before iteration,
 *                                   then built up node by node.
 * @param  normalize_lst  int*     — The source array of normalized integer values.
 * @param  n_elements     int      — Number of elements to read from `normalize_lst`
 *                                   and insert into the list.
 */
void linked_lst_creation(t_list **link_lst, int *normalize_lst, int n_elements)
{
	int		i;
	int		*content;
	t_list	*node;

	*link_lst = NULL;
	i = 0;
	while (i < n_elements)
	{
		content = ft_calloc(1, sizeof(int));
		if (!content)
			return ;
		*content = normalize_lst[i];
		node = ft_lstnew(content);
		if (!node)
		{
			ft_lstclear(link_lst, (*free));
			return ;
		}
		ft_lstadd_back(link_lst, node);
		i++;
	} 
}

/**
 * @brief  Replaces an integer array with its normalized-rank equivalent.
 *
 * @details  For each element at index `i`, counts how many other elements in the
 *           array are smaller than it — this count becomes its normalized rank.
 *           The result is stored in a newly allocated array. Once all ranks are
 *           computed, the original array is freed and `*lst` is updated to point
 *           to the normalized array.
 *
 * @param  lst        int** — Pointer to the integer array to normalize.
 * @param  n_elements int   — The number of elements in `*lst`.
 */
void	normalize(int **lst, int n_elements)
{
	int		*normalized_lst;
	int		total_min_val;
	size_t	i;
	size_t	j;

	if (!*lst || n_elements < 0)
		return ;
	normalized_lst = ft_calloc(n_elements, sizeof(int));
	if (!normalized_lst)
		return ;
	i = 0;
	while (i < (size_t)n_elements)
	{
		j = 0;
		total_min_val = 0;
		while (j < (size_t)n_elements)
		{
			if ((*lst)[j] < (*lst)[i])
				total_min_val++;
			j++;
		}
		normalized_lst[i++] = total_min_val;
	}
	free(*lst);
	*lst = normalized_lst;
}