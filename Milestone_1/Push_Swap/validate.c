#include "push_swap.h"

static void check_flag(int argc, char *argv[], int *is_flag);
static void check_int(int argc, char *argv[], int *is_flag);
static void check_duplicate_argv(int argc, char *argv[], int *is_flag);

void check_argv(int argc, char *argv[], int *is_flag)
{
	check_flag(argc, argv, is_flag);
	if (*is_flag > 2)
		print_error();
	check_int(argc, argv, is_flag);
	check_duplicate_argv(argc, argv, is_flag);
}

static void check_flag(int argc, char *argv[], int *is_flag)
{
	size_t i;

	i = 1;
	while (i < (unsigned long)argc)
	{
		if (argv[i][0] == '-' && argv[i][1] == '-')
		{
			if (ft_strncmp(argv[i], "--basic", ft_strlen("--basic") + 1) == 0)
				*is_flag += 1;
			else if (ft_strncmp(argv[i], "--medium", ft_strlen("--medium") + 1) == 0)
				*is_flag += 1;
			else if (ft_strncmp(argv[i], "--complex", ft_strlen("--complex") + 1) == 0)
				*is_flag += 1;
			else if (ft_strncmp(argv[i], "--adaptive", ft_strlen("--adaptive") + 1) == 0)
				*is_flag += 1;
			else if (ft_strncmp(argv[i], "--bench", ft_strlen("--bench") + 1) == 0)
				*is_flag += 1;
			else
				print_error();
		}
		i++;
	}
}

static void check_int(int argc, char *argv[], int *is_flag)
{
	size_t	i;
	long	n;

	i = 1 + *is_flag;
	while (i < (unsigned long)argc)
	{
		if (argv[i][0] != '-' && argv[i][1] != '-')
		{
			n = ft_atoi_strict(argv[i]);
			if (n < INT_MIN || n > INT_MAX)
				print_error();
		}
		i++;
	}
}

static void check_duplicate_argv(int argc, char *argv[], int *is_flag)
{
	size_t	i;
	size_t	j;

	(void)is_flag;
	i = 1;
	while (i < (unsigned long)argc)
	{
		j = i + 1;
		while (j < (unsigned long)argc)
		{
			if (ft_strncmp(argv[i], argv[j], ft_strlen(argv[i]) + 1) != 0)
				j++;
			else
				print_error();
		}
		i++;
	}
}
