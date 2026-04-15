#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "libft/libft.h"
# include <stdbool.h>

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
	bool		bench;
	int			n_flags;
}	t_flags;

typedef struct s_operations
{
	int	sa;
	int	sb;
	int	ss;
	int	pa;
	int	pb;
	int	ra;
	int	rb;
	int	rr;
	int	rra;
	int	rrb;
	int	rrr;
}	t_operations;

//Argument validation functions
int		check_argv(int argc, char *argv[], int **unsorted_lst, t_flags *flags);

//Utils functions
void	print_error(void);
long	ft_atoi_strict(const char *nptr);
int		ft_strcmp(const char *s1, const char *s2);
void	delete_content(void *content);
int		sum_operations(t_operations op);

//Maths utils functions
int		ft_sqrt(int nb);

//TO BE DELETED
//Printing functions to test
void	print_stack(t_list *stack, char *var_name);
void	print_flags(t_flags flags);
void	print_lst(int *lst, int n_elements, char *msg);
void	print_result(t_list *stack_a);

//Actions functions
void	sa(t_list **stack_a, t_operations *op, bool bench);
void	sb(t_list **stack_b, t_operations *op, bool bench);
void	ss(t_list **stack_a, t_list **stack_b, t_operations *op, bool bench);

void	pa(t_list **stack_a, t_list **stack_b, t_operations *op, bool bench);
void	pb(t_list **stack_b, t_list **stack_a, t_operations *op, bool bench);

void	ra(t_list **stack_a, t_operations *op, bool bench);
void	rb(t_list **stack_b, t_operations *op, bool bench);
void	rr(t_list **stack_a, t_list **stack_b, t_operations *op, bool bench);

void	rra(t_list **stack_a, t_operations *op, bool bench);
void	rrb(t_list **stack_b, t_operations *op, bool bench);
void	rrr(t_list **stack_a, t_list **stack_b, t_operations *op, bool bench);

//Alghoritm functions
void	bench(t_flags flags, t_operations op, float disorder);
void	select_strategy(t_list **stack_a, t_list **stack_b, t_flags *flags);
void	simple_strat(t_list **stack_a, t_list **stack_b,
			t_operations *op, t_flags *flags);
void	medium_strat(t_list **stack_a, t_list **stack_b,
			t_operations *op, t_flags *flags);
void	complex_strat(t_list **stack_a, t_list **stack_b,
			t_operations *op, t_flags *flags);
			
//Alghoritm utils 
int		find_max(t_list	*stack);
int		find_min(t_list	*stack);
float	compute_disorder(t_list *stack_a);
			
#endif