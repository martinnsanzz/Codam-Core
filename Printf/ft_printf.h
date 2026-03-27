#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <unistd.h>
# include <stdlib.h>
# include <stdarg.h> //This defines the macros va_start, va_arg, va_end, va_copy
# include "libft/libft.h"

int	ft_printf(const char *, ...);
int ft_printf_char(char c);
int	ft_printf_hex(int num, char conv);
int	ft_printf_int(int num, char conv);
int ft_printf_ptr(void *p);
int	ft_printf_str(char *s);

#endif