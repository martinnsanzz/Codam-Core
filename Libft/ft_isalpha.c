/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalpha.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:39:19 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/11 15:13:42 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Checks whether a character is an alphabetic letter.
*/
int	ft_isalpha(int c)
{
	c = (unsigned char)c;
	return ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'));
}
