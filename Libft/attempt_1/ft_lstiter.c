/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:41:22 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/19 14:11:44 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Applies function 'f' to the content of each node.
**
** Parameters:
** lst	: The address of a pointer to a node
** f	: The address of the function to apply to each node's
**		  content
**
** Behaviour:
** - Loops throught the list and modifies the content
**
** Returns:
** Nothing (void) function
*/
void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	t_list	*tmp;

	if (lst == NULL || f == NULL)
		return ;
	tmp = lst;
	while (tmp != NULL)
	{
		(*f)(tmp->content);
		tmp = tmp->next;
	}
}
