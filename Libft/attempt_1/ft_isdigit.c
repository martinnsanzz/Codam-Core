/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isdigit.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:39:25 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/11 15:13:48 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Checks whether a character is a decimal digit (0-9).
*/
int	ft_isdigit(int c)
{
	c = (unsigned char)c;
	return (c >= '0' && c <= '9');
}
