#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "libft/libft.h"

typedef enum e_strategy
{
	ADAPTIVE,
	SIMPLE,
	MEDIUM,
	COMPLEX
}	t_strategy;

typedef struct s_flags
{
	t_strategy	strategy;
	int			bench;
	int			n_flags;
}	t_flags;

//Argument validation functions
int		check_argv(int argc, char *argv[], int **unsorted_lst, t_flags *flags);

//Utils functions
void	print_error(void);
long	ft_atoi_strict(const char *nptr);
int		ft_strcmp(const char *s1, const char *s2);
void	delete_content(void *content);

//List functions
void	normalize(int **lst, int n_elements);
void	linked_lst_creation(t_list **link_lst, int *normalize_lst, int n_elements);

//TO BE DELETED
//Printing functions to test
void	print_link_lst(t_list *lst);
void	print_flags(t_flags flags);
void	print_lst(int *lst, int n_elements, char *msg);

#endif