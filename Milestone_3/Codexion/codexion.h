/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/02 12:47:09 by masanz-s          #+#    #+#             */
/*   Updated: 2026/09/07 13:19:44 by masanz-s         ###   ########.fr       */
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
# include <limits.h>

// ------------- Coder -------------
typedef struct s_coders{
	int id;
} t_coders;

// ---------- Validation -----------
int     	check_argv(int argc, char *argv[]);
int			check_valid_num(char *argv[]);
void		get_rules(char *argv[], int *arr, char **scheduler);

// ------------- Utils -------------
long long	ft_atoi(const char *nptr);
int			ft_strcmp(const char *s1, const char *s2);
size_t		ft_strlen(const char *s);
void		*ft_memset(void *s, int c, size_t n);
int			ft_isnumber(char *s);

#endif