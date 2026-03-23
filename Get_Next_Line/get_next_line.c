/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/21 19:07:55 by 2002mssm02        #+#    #+#             */
/*   Updated: 2026/03/23 18:32:02 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*get_next_line(int fd)
{
	char		buffer[BUFFER_SIZE + 1];
	char		*result;
	ssize_t		bytes;

	result = NULL;
	buffer[BUFFER_SIZE] = '\0'; 
	bytes = read(fd, buffer, BUFFER_SIZE);
	while (bytes > 0)
	{
		result = ft_strjoin(result, buffer);
		bytes = read(fd, buffer, BUFFER_SIZE);
		buffer[bytes] = '\0';
	}
	return (result);
}

#include <fcntl.h>
#include <stdio.h>

int	main(void)
{
	int		fd;
	char	*result;

	fd = open("test.txt", O_RDONLY);
	if (fd < 0)
	{
		printf("Failed to open file\n");
		return (0);
	}
	result = get_next_line(fd);
	printf("%s\n", result);
	// printf("%s\n", get_next_line(fd));
	// printf("%s\n", get_next_line(fd));
	close(fd);
	return (0);
}