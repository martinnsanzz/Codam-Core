/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:39:48 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/19 16:20:33 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Writes a single character to a file descriptor.
**
** Parameters:
** c  : character to write
** fd : file descriptor to write to
**
** Returns:
** Nothing (void).
**
** Behavior:
** - Writes exactly 1 byte to 'fd' using write(2)
**
** Note:
** No validation on 'fd' — passing an invalid or closed fd causes
** write(2) to fail silently (return value is ignored).
*/
void	ft_putchar_fd(char c, int fd)
{
	if (c == '\0')
		return ;
	write(fd, &c, 1);
}
