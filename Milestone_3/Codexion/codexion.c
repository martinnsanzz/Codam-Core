/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/02 12:47:12 by masanz-s          #+#    #+#             */
/*   Updated: 2026/09/07 15:19:58 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void create_threads(int *rules, pthread_t **threads);
void join_threads(int *rules, pthread_t **threads);
void *print_hello();

int     main(int argc, char *argv[])
{
    int			rules[7];
    char		*scheduler;
	pthread_t	*threads;

	if (check_argv(argc, argv) == -1)
        return (0);
    get_rules(argv, rules, &scheduler);

	threads = (pthread_t*) malloc(rules[0] * sizeof(pthread_t));
	if (threads == NULL)
		return (1);

	create_threads(rules, &threads);
	join_threads(rules, &threads);

	return (0);
}

void create_threads(int *rules, pthread_t **threads)
{
	int	i;

	i = 0;
	while(i < rules[0])
	{
		pthread_create(&(*threads)[i], NULL, print_hello, NULL);
		// pthread_join((*threads)[i], NULL);
		i++;
	}
}

void join_threads(int *rules, pthread_t **threads)
{
	int	i;

	i = 0;
	while(i < rules[0])
	{
		pthread_join((*threads)[i], NULL);
		i++;
	}
	free(*threads);
}

void *print_hello(){
	pthread_t thisThread = pthread_self();
	printf("Current thread ID: %lu\n", (unsigned long)thisThread);
	printf("Hello\n");
	sleep(1);
	return NULL;
}