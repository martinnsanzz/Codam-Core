/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:41:20 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/19 16:01:22 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Deletes a single linked list node and frees its memory.
**
** Parameters:
** lst : pointer to the node to delete
** del : function pointer used to free the node's content
**
** Returns:
** void
**
** Behavior:
** - Calls del on lst->content to free the content
** - Calls free on the node itself
** - Does NOT unlink the node from the list (caller's responsibility)
** - Returns early if lst is NULL
**
** Note:
** del must not be NULL (undefined behavior if NULL is passed).
** Does not affect neighboring nodes — caller must update surrounding
** pointers before calling this function to avoid dangling pointers.
*/
void	ft_lstdelone(t_list *lst, void (*del)(void*))
{
	if (lst == NULL || (*del) == NULL)
		return ;
	(*del)(lst->content);
	free(lst);
}
