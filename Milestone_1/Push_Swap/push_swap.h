#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

#include "libft/libft.h"

typedef struct s_stack
{
	int				content;
	struct s_stack	*next;
}	t_stack;

//Argument validation functions
void check_argv(int argc, char *argv[], int *is_flag);

//Utils functions
void	print_error();
long	ft_atoi_strict(const char *nptr);

#endif
 