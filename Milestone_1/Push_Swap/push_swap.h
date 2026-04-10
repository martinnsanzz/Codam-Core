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
void	linked_lst_creation(t_list **stack, int *normalize_lst, int n_elements);

//TO BE DELETED
//Printing functions to test
void	print_stack(t_list *stack);
void	print_flags(t_flags flags);
void	print_lst(int *lst, int n_elements, char *msg);

//Actions functions
void	sa(t_list **a);
void	sb(t_list **b);
void	ss(t_list **a, t_list **b);

void	pa(t_list **a, t_list **b);
void	pb(t_list **b, t_list **a);

void	ra(t_list **a);
void	rb(t_list **b);
void	rr(t_list **a, t_list **b);

void	rra(t_list **a);
void	rrb(t_list **b);
void	rrr(t_list **a, t_list **b);

//Alghoritm functions
void	select_strategy(t_list **stack_a, t_list **stack_b, t_flags flags);
void	simple_strat(t_list **a, t_list **b, int bench);
void	medium_strat(t_list **a, t_list **b, int bench);
void	complex_strat(t_list **a, t_list **b, int bench);

#endif