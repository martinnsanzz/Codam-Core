/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/02 12:47:09 by masanz-s          #+#    #+#             */
/*   Updated: 2026/09/03 16:17:43 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CODEXION_H
# define CODEXION_H

# include <aio.h>
# include <unistd.h>
# include <stdlib.h>
# include <stdio.h>
# include <sys/time.h>
# include <pthread.h>
# include <stdint.h>
// ------------- Utils -------------
int		ft_strcmp(const char *s1, const char *s2);
size_t	ft_strlen(const char *s);
int		ft_atoi(const char *nptr);
void	*ft_memset(void *s, int c, size_t n);
int		ft_isnumber(char *s);

#endif