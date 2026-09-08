/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: 2002mssm02 <2002mssm02@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/02 12:47:12 by masanz-s          #+#    #+#             */
/*   Updated: 2026/09/08 13:07:54 by 2002mssm02       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void create_threads(int *rules, pthread_t **threads);
void join_threads(int *rules, pthread_t **threads);
void *print_hello();

int COUNTER;
pthread_mutex_t lock;

int     main(int argc, char *argv[])
{
    int			rules[7];
    char		*scheduler;
	pthread_t	*threads;

	if (check_argv(argc, argv) == -1)
        return (0);
    get_rules(argv, rules, &scheduler);

	threads = ft_calloc(rules[0], sizeof(pthread_t));
	if (threads == NULL)
		return (1);
    pthread_mutex_init(&lock, NULL);
	create_threads(rules, &threads);
	join_threads(rules, &threads);
    
    pthread_mutex_destroy(&lock);
	return (0);
}

void create_threads(int *rules, pthread_t **threads)
{
	int	i;

	i = 0;
	while(i < rules[0])
		pthread_create(&(*threads)[i++], NULL, print_hello, NULL);
}

void join_threads(int *rules, pthread_t **threads)
{
	int	i;

	i = 0;
	while(i < rules[0])
		pthread_join((*threads)[i++], NULL);
	free(*threads);
}

void *print_hello(){
    pthread_mutex_lock(&lock);
    COUNTER += 1;
	pthread_t thisThread = pthread_self();
    printf("%d\n", COUNTER);
	printf("Current thread ID: %lu\n", (unsigned long)thisThread);
	printf("Hello\n");
	sleep(1);
    pthread_mutex_unlock(&lock);
	return NULL;
}