#include "push_swap.h"

void	normalize(int **lst, int n_elements)
{
	int		*normalized_lst;
	int		total_min_val;
	size_t	i;
	size_t	j;

	if (!lst)
		return ;
	normalized_lst = ft_calloc(n_elements, sizeof(int));
	if (!normalized_lst)
		return ;
	i = 0;
	while (i < (size_t)n_elements)
	{
		j = 0;
		total_min_val = 0;
		while (j < (size_t)n_elements)
		{
			if ((*lst)[j] < (*lst)[i])
				total_min_val++;
			j++;
		}
		normalized_lst[i++] = total_min_val;
	}
	free(*lst);
	*lst = normalized_lst;
}

long	ft_atoi_strict(const char *nptr)
{
	int		sign;
	long	num;

	sign = 1;
	num = 0;
	while (*nptr == ' ' || (*nptr >= 9 && *nptr <= 13))
		nptr++;
	if (*nptr == '+' || *nptr == '-')
	{
		if (*nptr == '-')
			sign *= -1;
		nptr++;
	}
	if (!ft_isdigit(*nptr))
		print_error();
	while (*nptr >= '0' && *nptr <= '9')
	{
		num = num * 10 + (*nptr - '0');
		nptr++;
	}
	if (*nptr != '\0')
		print_error();
	return (num * sign);
}

int	ft_strcmp(const char *s1, const char *s2)
{
	size_t	i;

	i = 0;
	if (!s1 || !s2)
		return (0);
	while (s1[i] != '\0' || s2[i] != '\0')
	{
		if (s1[i] != s2[i])
			return ((unsigned char)s1[i] - (unsigned char)s2[i]);
		i++;
	}
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}

void	print_error(void)
{
	ft_putstr_fd("Error\n", 2);
	exit (1);
}
