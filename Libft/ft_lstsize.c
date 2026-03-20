/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:41:33 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/16 15:38:15 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Counts the number of nodes in a linked list.
**
** Parameter:
** lst : pointer to the first node of the list
**
** Returns:
** The total number of nodes in the list.
*/
int	ft_lstsize(t_list *lst)
{
	int		size;

	size = 0;
	while (lst != NULL)
	{
		lst = lst->next;
		size++;
	}
	return (size);
}
