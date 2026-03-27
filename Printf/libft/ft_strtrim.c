/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: 2002mssm02 <2002mssm02@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:40:43 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/27 11:53:04 by 2002mssm02       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	char	*s1_trim;
	size_t	start;
	size_t	end;
	size_t	size;

	start = 0;
	end = ft_strlen(s1);
	if (end == 0)
		return (s1_trim = ft_calloc(1, sizeof(char)));
	while (s1[start] && ft_strchr(set, s1[start]))
		start++;
	while (end > start && ft_strchr(set, s1[end - 1]))
		end--;
	size = end - start;
	s1_trim = ft_calloc(size + 1, sizeof(char));
	if (s1_trim == NULL)
		return (NULL);
	s1_trim = ft_memcpy(s1_trim, &s1[start], size);
	return (s1_trim);
}
