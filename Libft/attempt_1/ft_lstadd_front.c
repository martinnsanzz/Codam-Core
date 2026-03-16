/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:41:14 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/16 15:35:15 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Adds the node 'new' at the beginning of the list.
**
** Parameters:
** lst : pointer to the head pointer of the list
** new : node to insert at the front of the list
**
** Behavior:
** The new node becomes the first element of the list.
** Its next pointer is set to the previous head.
*/
void	ft_lstadd_front(t_list **lst, t_list *new)
{
	if (new == NULL)
		return ;
	new->next = *lst;
	*lst = new;
}
