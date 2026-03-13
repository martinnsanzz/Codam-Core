/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: 2002mssm02 <2002mssm02@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:40:47 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/13 14:14:50 by 2002mssm02       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Converts a uppercase ASCII letter to it lowercase equivelant.
**
** Parameter:
**	c: char value to convert
**
** Return:
** The lowercase version of the character if it is a uppercase letter.
** Otherwise, the input value is returned unchanged.

** Notes:
** The input is cast to unsigned char to ensure correct behavior
** when c is outside the standard ASCII range.
*/
int	ft_tolower(int c)
{
	c = (unsigned char)c;
	if (c >= 'A' && c <= 'Z')
		return (c + 32);
	return (c);
}
