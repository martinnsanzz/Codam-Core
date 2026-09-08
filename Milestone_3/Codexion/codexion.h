/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: 2002mssm02 <2002mssm02@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/02 12:47:09 by masanz-s          #+#    #+#             */
/*   Updated: 2026/09/08 11:16:12 by 2002mssm02       ###   ########.fr       */
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

// ------------ Display ------------
void        display_status(int timestamp_ms, int coder_id, char *state);

// ------------- Utils -------------
long long	ft_atoi(const char *nptr);
int			ft_strcmp(const char *s1, const char *s2);
size_t		ft_strlen(const char *s);
void		*ft_memset(void *s, int c, size_t n);
int			ft_isnumber(char *s);
void        ft_bzero(void *s, size_t n);
void        *ft_calloc(size_t nmemb, size_t size);
char        *ft_itoa(int num);

#endif