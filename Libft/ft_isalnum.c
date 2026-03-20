/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalnum.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:39:16 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/11 15:15:46 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Checks whether a character is an alphanumeric character.
** An alphanumeric character is either a letter (A-Z, a-z)
** or a digit (0-9).
*/
int	ft_isalnum(int c)
{
	c = (unsigned char)c;
	return (ft_isalpha(c) || ft_isdigit(c));
}
