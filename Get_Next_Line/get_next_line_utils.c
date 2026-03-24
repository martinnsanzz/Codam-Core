/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/21 19:08:31 by 2002mssm02        #+#    #+#             */
/*   Updated: 2026/03/24 15:47:53 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

/*
** Copies n amount of character to dest from src
**
** Parameters:
** dest		: String to copy to
** src		: Null terminated string to copy from
** n		: Amount of characters to be copied
**
** Returns:
** Copied string
*/
char	*ft_strncpy(char *dest, const char *src, size_t n)
{
	unsigned int	i;

	if (src == NULL)
		return (NULL);
	i = 0;
	while (i < n)
	{
		dest[i] = src[i];
		i++;
	}
	return (dest);
}

/*
** Allocates and returns a new string with 's1' as prefix and
** 's2' as suffix
**
** Parameters:
** s1: The prefix string.
** s2: The suffix string.
**
** Returns:
** The new string.
** NULL if the allocation fails.
*/
char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*str;
	int		total_len;
	int		i;

	if (!s1)
		s1 = "";
	total_len = ft_strlen(s1) + ft_strlen(s2);
	str = ft_calloc(total_len + 1, sizeof(char));
	if (str == NULL)
		return (NULL);
	i = 0;
	while (*s1 != '\0')
		str[i++] = *s1++;
	while (*s2 != '\0')
		str[i++] = *s2++;
	return (str);
}

/*
** Allocates memory for an array of 'nmemb' elements of 'size' bytes each.
** The allocated memory block is initialized to zero.
**
** Parameters:
** nmemb : number of elements to allocate
** size  : size in bytes of each element
**
** Returns:
** A pointer to the allocated memory initialized to zero.
** NULL if the allocation fails or memory overflow is detected.
**
** Note:
** The memory is initialized to zero using ft_bzero.
*/
void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*ptr;

	if (nmemb == 0 || size == 0)
		return (malloc(0));
	if (nmemb > SIZE_MAX / size)
		return (NULL);
	ptr = malloc(nmemb * size);
	if (ptr == NULL)
		return (NULL);
	ft_bzero(ptr, nmemb * size);
	return (ptr);
}

/*
** Computes the length of a null-terminated string.
** Parameters:
** s	: null-terminated string to measure
**
** Returns:
** Number of characters in the string, excluding the terminating '\0'.
*/
size_t	ft_strlen(const char *s)
{
	size_t	len;

	len = 0;
	while (s[len] != '\0')
		len++;
	return (len);
}

/*
** Null terminates '\0' the first n bytes of the memory area pointed to by s
** 
** Parameters:
** s : pointer to the memory block to modify
** n : number of bytes to write
**
** Note:
** Memory is written byte-by-byte, therefore the pointer is cast
** to unsigned char* to allow single-byte access.
*/
void	ft_bzero(void *s, size_t n)
{
	size_t			i;
	unsigned char	*ptr;

	ptr = (unsigned char *)s;
	i = 0;
	while (i < n)
	{
		ptr[i] = '\0';
		i++;
	}
}

/*
** Extracts the next line from the buffer, including the newline character.
**
** Parameters:
** buffer : null-terminated string containing buffered file content
**
** Returns:
** A newly allocated null-terminated string containing the line.
** NULL if buffer is NULL, empty, or allocation fails.
**
** Behavior:
** - If a '\n' is found, copies only up to (including) the newline
** - If no '\n' is found, copies the entire buffer content
** - Allocates len + 1 bytes (ft_calloc zeroes the buffer, null-term is implicit)
**
** Note:
** Caller is responsible for freeing the returned string.
*/
char	*extract_line(char	*buffer)
{
	char	*line;
	char	*new_line;
	size_t	len;

	if (buffer == NULL || buffer[0] == '\0')
		return (NULL);
	line = ft_strchr(buffer, '\n');
	if (line == NULL)
		len = ft_strlen(buffer);
	else
		len = line - buffer + 1;
	new_line = ft_calloc(len + 1, sizeof(char));
	if (new_line == NULL)
		return (NULL);
	ft_strncpy(new_line, buffer, len);
	return (new_line);
}

char	*trim_buffer(char *buffer)
{
	char	*new_line;

	if (buffer == NULL || buffer[0] == '\0')
		return (NULL);
// 	Write it from scratch using ft_strchr. The logic is:

// Find \n in buffer
// If not found → return empty string (or ft_calloc(1, 1))
// If found → copy everything after it into a new allocation
// Return that
	
}

/*
** Finds a character inside a string and returns a pointer to that location
**
** Parameters:
** c	: Character to find
** s	: Null terminate dstring to look at
**
** Returns:
** Pointer to the character found in the string
** Null if nothing is found
*/
char	*ft_strchr(const char *s, int c)
{
	int		i;
	char	*str;

	c = (unsigned char)c;
	str = (char *)s;
	i = 0;
	while (str[i])
	{
		if (c == str[i])
			return (&str[i]);
		i++;
	}
	if (c == str[i])
		return (&str[i]);
	return (NULL);
}

// #include <stdio.h>

// int main(void)
// {
// 	char	*src = "Hello \n";
// 	char	*dest;

// 	dest = extract_line(src);
// 	printf("%s", dest);
// 	return (0);
// }