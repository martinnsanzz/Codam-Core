/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:39:13 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/19 11:25:25 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Allocates memory for an array of 'nmemb' elements of 'size' bytes each.
** The allocated memory block is initialized to zero.
**
** Parameters:
** nmemb : number of elements to allocate
** size  : size in bytes of each element
**
** Returns:
** A pointer to the allocated memory initialized to zero.
** NULL if the allocation fails or memory overflow is detected.
**
** Note:
** The memory is initialized to zero using ft_bzero.
*/
void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*ptr;

	if (nmemb == 0 || size == 0)
		return (malloc(0));
	if (nmemb > SIZE_MAX / size)
		return (NULL);
	ptr = malloc(nmemb * size);
	if (ptr == NULL)
		return (NULL);
	ft_bzero(ptr, nmemb * size);
	return (ptr);
}
