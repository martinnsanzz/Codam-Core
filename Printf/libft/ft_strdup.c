/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: 2002mssm02 <2002mssm02@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:40:02 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/27 11:53:46 by 2002mssm02       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	char	*str_dup;
	int		s_len;
	int		i;

	s_len = ft_strlen(s);
	str_dup = (char *)malloc(sizeof(char) * (s_len + 1));
	if (str_dup == NULL)
		return (NULL);
	i = 0;
	while (s[i] != '\0')
	{
		str_dup[i] = s[i];
		i++;
	}
	str_dup[i] = '\0';
	return (str_dup);
}
