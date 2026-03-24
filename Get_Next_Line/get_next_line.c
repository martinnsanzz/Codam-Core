/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/21 19:07:55 by 2002mssm02        #+#    #+#             */
/*   Updated: 2026/03/24 15:43:35 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*get_next_line(int fd)
{
	static char	*buffer;
	char		*result;
	ssize_t		bytes;

	result = NULL;
	if (buffer == NULL)
	{
		buffer = ft_calloc(BUFFER_SIZE + 1, sizeof(char));
		if (buffer == NULL)
			return (NULL);
	}
	bytes = read(fd, buffer, BUFFER_SIZE);
	result = extract_line(buffer);
	if (result == NULL)
		return (NULL);
	return (result);
}

#include <fcntl.h>
#include <stdio.h>

int	main(void)
{
	int		fd;
	int		i;
	int		j;
	char	*line;
	char	*test_dir = "test_files/";
	char	*test_files[] = {"test_single_line.txt", "test_multi_short.txt",
							"test_long_lines.txt", "test_empty_lines.txt",
							"test_no_trailing_newline.txt", "test_single_chars.txt",
							"test_only_newlines.txt", "test_mixed_lengths.txt",
							"test_buffer_boundary.txt", "test_single_newline.txt"};
	
	i = 0;
	while (test_files[i] != (void *)0 && i < 1)
	{
		printf("========================================\n");
		printf("File %s\n", test_files[i]);
		printf("========================================\n");
		fd = open(ft_strjoin(test_dir, test_files[i]), O_RDONLY);
		if (fd < 0)
		{
			printf("Failed to open file\n");
			return (0);
		}
		line = "";
		j = 1;
		while (line != NULL)
		{
			line = get_next_line(fd);
			printf("%d: %s", j, line);
			j++;
		}
		printf("\n");
		i++;
	}
}