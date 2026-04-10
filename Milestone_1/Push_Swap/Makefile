.DEFAULT_GOAL := all

NAME = push_swap
DEBUGEXEC = a.out.debug
LIBFTLIB = libft.a

LIBFT_DIR = libft
OBJS_DIR = objs
STACK_OP_DIR = stack_operations
STRATS_DIR = strats
TESTING_UTILS_DIR = testing_utils

SRCS = $(wildcard *.c) \
		$(wildcard $(STACK_OP_DIR)/*.c) \
		$(wildcard $(TESTING_UTILS_DIR)/*.c) \
		$(wildcard $(STRATS_DIR)/*.c)
OBJS = $(SRCS:%.c=$(OBJS_DIR)/%.o)

CC = cc
CFLAGS = -Wall -Werror -Wextra
GDBFLAG = -g
RM = rm -rf
AR = ar -rcs
LIBFTLINK = -L$(LIBFT_DIR) -lft

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) $(LIBFTLINK) -o $(NAME)

$(DEBUGEXEC): $(OBJS)
	$(CC) $(GDBFLAG) $(OBJS) $(LIBFTLINK) -o $(DEBUGEXEC)

$(OBJS_DIR)/%.o: %.c
	mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(GDBFLAG) -c $< -o $@

$(OBJS_DIR):
	mkdir -p $(OBJS_DIR)

$(LIBFTLIB):
	$(MAKE) -C $(LIBFT_DIR) CFLAGS="$(CFLAGS) $(GDBFLAG)"

all: libft $(NAME)

debug: libft $(DEBUGEXEC)

libft: $(LIBFTLIB)

clean:
	$(RM) $(OBJS_DIR)
	$(MAKE) -C $(LIBFT_DIR) clean

fclean: clean
	$(RM) $(NAME) $(DEBUGEXEC)
	$(MAKE) -C $(LIBFT_DIR) fclean

re: fclean all

.PHONY: all clean fclean re debug