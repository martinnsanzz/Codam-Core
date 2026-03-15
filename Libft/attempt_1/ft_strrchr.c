/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: 2002mssm02 <2002mssm02@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:40:40 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/15 19:15:58 by 2002mssm02       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	int		len;
	char	*str;

	c = (char)c;
	str = (char *)s;
	len = ft_strlen(str);
	if (c == str[len])
		return (&str[len]);
	while (len >= 0)
	{
		if (c == str[len])
			return (&str[len]);
		len--;
	}
	return (NULL);
}
