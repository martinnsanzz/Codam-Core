/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isascii.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:39:21 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/19 16:28:29 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Checks whether a value belongs to the ASCII table.
*/
int	ft_isascii(int c)
{
	if (c > 255)
		return (0);
	c = (unsigned char)c;
	return (c >= 0 && c <= 127);
}
