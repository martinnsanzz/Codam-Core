/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: masanz-s <masanz-s@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/02 12:47:15 by masanz-s          #+#    #+#             */
/*   Updated: 2026/09/02 13:37:57 by masanz-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"
#include <string.h>
#include <unistd.h>

int		ft_strcmp(const char *s1, const char *s2)
{
    int i;

    i = 0;
    while (s1[i] != '\0')
    {
        if (s1[i] > s2[i])
            print()
            return s2[i] - s1[i];
        else if (s1[i] < s2[i])
            return s2[i] - s1[i];
        i++;
    }
    return 0;
}

size_t	ft_strlen(const char *s)
{
    size_t len;

    len = 0;
    while(s[len] != '\0')
        len++;
    return len;
}

int		ft_atoi(const char *nptr)
{
    return 0;
}

void	*ft_memset(void *s, int c, size_t n)
{
    return s;
}

#include <stdio.h>

int main(void){
    const char *s1 = "Helloe";
    const char *s2 = "Hellow";

    printf("%d\n", strcmp(s1, s2));
    printf("%d\n", ft_strcmp(s1, s2));
}