/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: 2002mssm02 <2002mssm02@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:40:00 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/15 20:22:01 by 2002mssm02       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Searches for the first occurrence of character c in the string s.
**
** Parameters:
** s : null-terminated string to search
** c : character to locate in the string
**
** Returns:
** A pointer to the first occurrence of c in s.
** NULL if the character is not found.
**
** Notes:
** c is cast to char to match the type stored in the string.
** The function also checks the terminating '\0', allowing
** searches for the null terminator.
*/
char	*ft_strchr(const char *s, int c)
{
	int		i;
	char	*str;

	c = (char)c;
	str = (char *)s;
	i = 0;
	while (str[i])
	{
		if (c == str[i])
			return (&str[i]);
		i++;
	}
	if (c == str[i])
		return (&str[i]);
	return (NULL);
}
