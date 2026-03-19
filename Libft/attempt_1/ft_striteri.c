/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_striteri.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:40:05 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/19 16:30:06 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Applies a function to each character of a string, modifying it in-place.
**
** Parameters:
** s : input null-terminated string (modified in-place via pointer)
** f : function pointer called with (index, char *) for each character
**
** Returns:
** Nothing (void).
**
** Behavior:
** - Passes a pointer to each character of 's' alongside its unsigned int index
** - Allows 'f' to modify the character directly through the pointer
** - Does nothing if 's' is NULL
**
** Note:
** Unlike ft_strmapi, no allocation occurs — 's' is mutated directly.
** Behavior is undefined if 'f' is NULL.
*/
void	ft_striteri(char *s, void (*f)(unsigned int, char*))
{
	unsigned int	i;

	i = 0;
	if (s == NULL || (*f) == NULL)
		return ;
	while (i < ft_strlen(s))
	{
		(*f)(i, &s[i]);
		i++;
	}
}
