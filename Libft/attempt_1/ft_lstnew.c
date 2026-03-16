/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:41:30 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/16 15:35:09 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Allocates and initializes a new list node.
**
** Parameters:
** content : pointer to the data to store in the new node
**
** Returns:
** - A pointer to the newly created node.
** - NULL if memory allocation fails.
**
** Notes:
** The content pointer is stored directly and not duplicated.
** The next pointer is initialized to NULL.
*/
t_list	*ft_lstnew(void *content)
{
	t_list	*node;

	node = (t_list *)malloc(sizeof(t_list));
	if (node == NULL)
		return (NULL);
	node->content = content;
	node->next = NULL;
	return (node);
}
