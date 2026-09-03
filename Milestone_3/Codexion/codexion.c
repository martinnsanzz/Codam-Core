/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/02 12:47:12 by masanz-s          #+#    #+#             */
/*   Updated: 2026/09/03 16:14:43 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int check_argv(int argc, char *argv[]);

int main(int argc, char *argv[])
{
	check_argv(argc, argv);

	return 0;
}

int check_argv(int argc, char *argv[])
{
	fprintf(stderr, "\033[0;31m");
	if (argc != 9){
		fprintf(stderr, "Program must run with contain 9 arguments !!\n"
						"	Run make help-run for help.\n");
		return (0);
	}
	else if ((ft_strcmp(argv[8], "fifo")) && (ft_strcmp(argv[8], "edf"))){
		fprintf(stderr, "Wrong scheduler {%s}: Allowed ['fifo', 'edf']\n", argv[8]);
		return (0);
	}

	int i;

	i = 0;
	while (i++ < 7){
		if (ft_isnumber(argv[i]) == 0){
			fprintf(stderr, "Argument %d is an invalid int: {%s}\n", i, argv[i]);
			return (0);
		}
		else if (ft_atoi(argv[i]) < 0 && ft_atoi(argv[i]) > INT_MAX)
	}
	fprintf(stderr, "\033[0m");
	return (1);
}