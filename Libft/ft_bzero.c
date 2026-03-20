/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:39:11 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/12 14:00:49 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Null terminates '\0' the first n bytes of the memory area pointed to by s
** 
** Parameters:
** s : pointer to the memory block to modify
** n : number of bytes to write
**
** Note:
** Memory is written byte-by-byte, therefore the pointer is cast
** to unsigned char* to allow single-byte access.
*/
void	ft_bzero(void *s, size_t n)
{
	size_t			i;
	unsigned char	*ptr;

	ptr = (unsigned char *)s;
	i = 0;
	while (i < n)
	{
		ptr[i] = '\0';
		i++;
	}
}
