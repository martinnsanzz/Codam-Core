.DEFAULT_GOAL := all

NAME = push_swap
LIBFTLIB = libft.a

LIBFT_DIR = libft
OBJS_DIR = objs

SRCS = $(wildcard *.c)
OBJS = $(SRCS:%.c=$(OBJS_DIR)/%.o)

CC = cc
CFLAGS = -Wall -Werror -Wextra
RM = rm -rf
AR = ar -rcs
LIBFTLINK = -L$(LIBFT_DIR) -lft

$(NAME): $(LIBFTLIB)
	$(CC) $(CFLAGS) $(SRCS) $(LIBFTLINK) -o $(NAME)

$(OBJS_DIR)/%.o: %.c | $(OBJS_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJS_DIR):
	mkdir -p $(OBJS_DIR)

$(LIBFTLIB):
	$(MAKE) -C $(LIBFT_DIR)

all: libft $(NAME)

libft: $(LIBFTLIB)

clean:
	$(RM) $(OBJS_DIR)
	$(MAKE) -C $(LIBFT_DIR) clean

fclean: clean
	$(RM) $(NAME)
	$(MAKE) -C $(LIBFT_DIR) fclean

re: fclean all

.PHONY: all clean fclean re