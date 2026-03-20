/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isprint.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:39:32 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/11 15:13:52 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Checks whether a character is printable.
** Printable ASCII range: 32 (space) to 126 (~).
*/
int	ft_isprint(int c)
{
	c = (unsigned char)c;
	return (c >= ' ' && c <= '~');
}
