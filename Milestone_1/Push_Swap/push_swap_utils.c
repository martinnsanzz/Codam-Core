#include "push_swap.h"

/**
 * @brief  Replaces an integer array with its normalized-rank equivalent.
 *
 * @details  For each element at index `i`, counts how many other elements in the
 *           array are smaller than it — this count becomes its normalized rank.
 *           The result is stored in a newly allocated array. Once all ranks are
 *           computed, the original array is freed and `*lst` is updated to point
 *           to the normalized array.
 *
 * @param  lst        int** — Pointer to the integer array to normalize.
 * @param  n_elements int   — The number of elements in `*lst`.
 */
void	normalize(int **lst, int n_elements)
{
	int		*normalized_lst;
	int		total_min_val;
	size_t	i;
	size_t	j;

	if (!*lst || n_elements < 0)
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

/**
 * @brief  Converts a string to a long integer with strict format validation.
 *
 * @details  Skips leading whitespace (spaces and ASCII 9–13), then parses an
 *           optional sign character. Calls `print_error` and exits
 *           if the first non-sign character is not a digit, or if any non-digit
 *           character is found after the numeric sequence. Returns the parsed
 *           value with the correct sign applied.
 *
 * @return long — The parsed integer value on success, with sign applied.
 *                Never returns on invalid input.
 */
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

/**
 * @brief  Compares two null-terminated strings lexicographically.
 *
 * @details  Iterates through both strings simultaneously until a differing
 *           character is found or both strings reach '\0'.
 * 
 * @return int — 0 if both strings are equal.
 *               Positive value if the differing character in s1 > s2.
 *               Negative value if the differing character in s1 < s2.
 */
int	ft_strcmp(const char *s1, const char *s2)
{
	size_t	i;

	i = 0;
	while (s1[i] != '\0' && s2[i] != '\0')
	{
		if (s1[i] != s2[i])
			return ((unsigned char)s1[i] - (unsigned char)s2[i]);
		i++;
	}
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}

/**
 * @brief When called it prints 'Error' to stderr (2) and 
 * 		  exits the program. The user decides when to call
 * 		  this function.
 */
void	print_error(void)
{
	ft_putstr_fd("Error\n", 2);
	exit (1);
}
