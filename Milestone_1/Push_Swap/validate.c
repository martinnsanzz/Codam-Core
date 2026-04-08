#include "push_swap.h"

static void	check_flag(int argc, char *argv[], t_flags *flags);
static void	check_int(int argc, char *argv[]);
static void	check_duplicate_argv(int argc, char *argv[], int **unsorted_lst);
static void	int_array(int argc, char *argv[], int **unsorted_lst);

void	check_argv(int argc, char *argv[], int **unsorted_lst, t_flags *flags)
{
	check_flag(argc, argv, flags);
	if (flags->n_flags > 2)
		print_error();
	check_int(argc, argv);
	check_duplicate_argv(argc, argv, unsorted_lst);
}

static void	check_flag(int argc, char *argv[], t_flags *flags)
{
	size_t	i;

	i = 1;
	while (i < (unsigned long)argc)
	{
		if (argv[i][0] == '-' && argv[i][1] == '-')
		{
			if (!ft_strcmp(argv[i], "--simple"))
				flags->strategy = SIMPLE;
			else if (!ft_strcmp(argv[i], "--medium"))
				flags->strategy = MEDIUM;
			else if (!ft_strcmp(argv[i], "--complex"))
				flags->strategy = COMPLEX;
			else if (!ft_strcmp(argv[i], "--adaptive"))
				flags->strategy = ADAPTIVE;
			else if (!ft_strcmp(argv[i], "--bench"))
				flags->bench += 1;
			else
				print_error();
			flags->n_flags += 1;
		}
		i++;
	}
}

static void	check_int(int argc, char *argv[])
{
	size_t	i;
	long	n;

	i = 1;
	while (i < (unsigned long)argc)
	{
		if (argv[i][0] != '-' || argv[i][1] != '-')
		{
			n = ft_atoi_strict(argv[i]);
			if (n < INT_MIN || n > INT_MAX)
				print_error();
		}
		i++;
	}
}

static void	check_duplicate_argv(int argc, char *argv[], int **unsorted_lst)
{
	size_t	i;
	size_t	j;

	i = 1;
	int_array(argc, argv, unsorted_lst);
	while (i < (unsigned long)argc)
	{
		j = i + 1;
		while (j < (unsigned long)argc)
		{
			if (argv[i][0] != '-' || argv[i][1] != '-')
			{
				if ((*unsorted_lst)[i - 1] == (*unsorted_lst)[j - 1])
					print_error();
			}
			else
				if (!ft_strcmp(argv[i], argv[j]))
					print_error();
			j++;
		}
		i++;
	}
}

static void	int_array(int argc, char *argv[], int **unsorted_lst)
{
	int		n_elements;
	size_t	i;
	size_t	j;

	i = 1;
	n_elements = 0;
	while (i < (unsigned long)argc)
	{
		if (argv[i][0] != '-' || argv[i][1] != '-')
			n_elements++;
		i++;
	}
	*unsorted_lst = ft_calloc(n_elements, sizeof(int));
	if (!*unsorted_lst)
		exit(1);
	i = 1;
	j = 0;
	while (i < (unsigned long)argc)
	{
		if (argv[i][0] != '-' || argv[i][1] != '-')
			(*unsorted_lst)[j++] = ft_atoi(argv[i]);
		i++;
	}
}
