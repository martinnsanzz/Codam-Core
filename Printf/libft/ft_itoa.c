/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: 2002mssm02 <2002mssm02@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 09:39:34 by masanz-s          #+#    #+#             */
/*   Updated: 2026/03/27 11:55:19 by 2002mssm02       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	num_len(int num);

char	*ft_itoa(int n)
{
	char	*num;
	long	nb;
	size_t	len;

	nb = n;
	len = num_len(nb) + (nb < 0);
	num = ft_calloc(len + 1, sizeof(char));
	if (num == NULL)
		return (NULL);
	if (nb < 0)
	{
		num[0] = '-';
		nb *= -1;
	}
	while (len > (n < 0))
	{
		num[--len] = (nb % 10) + '0';
		nb /= 10;
	}
	return (num);
}

static size_t	num_len(int num)
{
	size_t	len;
	long	nbum;

	len = 1;
	nbum = num;
	if (nbum < 0)
		nbum *= -1;
	while (nbum >= 10)
	{
		len++;
		nbum /= 10;
	}
	return (len);
}
