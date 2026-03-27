/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: 2002mssm02 <2002mssm02@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:39:45 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/27 11:54:19 by 2002mssm02       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *s, int c, size_t n)
{
	unsigned char	c_char;
	unsigned char	*ptr;

	c_char = (unsigned char)c;
	ptr = (unsigned char *)s;
	while (n--)
		*ptr++ = c_char;
	return (s);
}
