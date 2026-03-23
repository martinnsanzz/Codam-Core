/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/21 19:08:31 by 2002mssm02        #+#    #+#             */
/*   Updated: 2026/03/23 19:36:31 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_strdup(const char *s)
{
	char	*str_dup;
	int		s_len;
	int		i;

	s_len = ft_strlen(s);
	str_dup = (char *)malloc(sizeof(char) * (s_len + 1));
	if (str_dup == NULL)
		return (NULL);
	i = 0;
	while (s[i] != '\0')
	{
		str_dup[i] = s[i];
		i++;
	}
	str_dup[i] = '\0';
	return (str_dup);
}

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

size_t	ft_strlen(const char *s)
{
	size_t	len;

	len = 0;
	while (s[len] != '\0')
		len++;
	return (len);
}

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

char	*ft_strcpy(char *dest, const char *src)
{
	size_t	i;
	size_t	len;

	i = 0;
	len = ft_strlen(src);
	dest = ft_calloc(len + 1, sizeof(char));
	while (*src != '\0')
	{
		dest[i++] = *src++;
	}
	return (&dest[0]);
}

// #include <stdio.h>

// int main(void)
// {
// 	char	*src = "Hello";
// 	char	*dest = NULL;

// 	dest = ft_strjoin(dest, src);
// 	printf("%s\n", dest);
// 	return (0);
// }