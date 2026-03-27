/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: 2002mssm02 <2002mssm02@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/27 11:15:46 by 2002mssm02        #+#    #+#             */
/*   Updated: 2026/03/27 11:28:39 by 2002mssm02       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <unistd.h>
# include <stdlib.h>
# include <stdarg.h> //This defines the macros va_start, va_arg, va_end, va_copy
# include "libft/libft.h"

int	ft_printf(const char *, ...);

#endif