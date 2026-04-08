#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

#include "libft/libft.h"

typedef enum e_strategy
{
    ADAPTIVE,
    SIMPLE,
    MEDIUM,
    COMPLEX
}   t_strategy;

typedef struct s_flags
{
    t_strategy  strategy;
    int         bench;
	int			n_flags;
}   t_flags;

//Argument validation functions
void check_argv(int argc, char *argv[], t_flags *flags);

//Utils functions
void	print_error(void);
long	ft_atoi_strict(const char *nptr);
int		ft_strcmp(const char *s1, const char *s2);

#endif
 