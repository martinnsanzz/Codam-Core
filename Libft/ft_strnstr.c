/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:40:39 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/16 10:41:15 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** searches for the first occurrence of little inside big, 
** but only within the first len characters.
**
** Parameters:
**	big		: null-terminated string to search in
**	little	: null-terminated string to search
**	len 	: maximum number of characters of big to search
**
** Returns:
** - A pointer to the first occurrence of 'little' in 'big'
** - NULL if 'little' is not found within the first len characters
** - A pointer to 'big' if 'little' is an empty string
*/
char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	i;
	size_t	j;

	i = 0;
	if (little[i] == '\0')
		return ((char *)&big[i]);
	while (i < len && big[i] != '\0')
	{
		j = 0;
		if (big[i] == little[j])
		{
			while (big[i + j] == little[j] && (i + j) < len)
			{
				if (little[j + 1] == '\0')
					return ((char *)&big[i]);
				j++;
			}
		}
		i++;
	}
	return (NULL);
}
