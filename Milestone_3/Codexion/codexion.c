/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/02 12:47:12 by masanz-s          #+#    #+#             */
/*   Updated: 2026/09/10 14:58:51 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int		init_coders(int num_coders, t_coders **coders);
int		init_values(int num_coders, pthread_t **threads, pthread_mutex_t **dongles);
void	clean_values(int num_coders, t_coders **coders, pthread_t **threads,
					 pthread_mutex_t **dongles);
void	*print_hello();

int     main(int argc, char *argv[])
{
    int				rules[7];
    char			*scheduler;
	t_coders		*coders;
	pthread_t		*threads;
	pthread_mutex_t	*dongles;

	if (check_argv(argc, argv) == -1)
        return (0);
    get_rules(argv, rules, &scheduler);

	if (init_values(rules[0], &coders, &threads, &dongles))
		return (1);
	clean_values(rules[0], &coders, &threads, &dongles);

	return (0);
}

int	init_coders(int num_coders, t_coders **coders)
{
	*coders = ft_calloc(num_coders, sizeof(t_coders));
	if (*coders == NULL)
		return (1);

	while(num_coders--)
		(*coders)[num_coders].id = (num_coders + 1);

	return (0);
}

int	init_values(int num_coders, pthread_t **threads, pthread_mutex_t **dongles)
{
	int	tmp;

	*threads = ft_calloc(num_coders, sizeof(pthread_t));
	*dongles = ft_calloc(num_coders, sizeof(pthread_mutex_t));

	if (*threads == NULL || *dongles == NULL)
		return (1);

	tmp = num_coders;
	while(num_coders--){
		(*coders)[num_coders].id = (num_coders + 1);
		pthread_mutex_init(&(*dongles)[num_coders], NULL);
	}

	num_coders = tmp;
	while(num_coders--){
		if (pthread_create(&(*threads)[num_coders], NULL, print_hello, NULL)){
			fprintf(stderr, "\033[0;31mFailed to create"
							"thread number: {%d}\n\033[0m", num_coders);
			return (1);
		}
	}
	return (0);
}

void	clean_values(int num_coders, t_coders **coders, pthread_t **threads,
					 pthread_mutex_t **dongles)
{
	while(num_coders--)
	{
		pthread_join((*threads)[num_coders], NULL);
		pthread_mutex_destroy(&(*dongles)[num_coders]);
	}
	free(*threads);
	free(*dongles);
	free(*coders);
}

void	*print_hello(){
	pthread_t thisThread = pthread_self();
	printf("Current thread ID: %lu\n", (unsigned long)thisThread);
	printf("Hello\n");
	sleep(1);
	return NULL;
}