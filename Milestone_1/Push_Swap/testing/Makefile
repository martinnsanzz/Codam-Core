.DEFAULT_GOAL := all

EXEC = a.out
EXECDEBUG = a.out.debug

LIBFTLIB = libft.a

SRC_DIR = ../
LIBFT_DIR = ../libft
OBJS_DIR = objs

SRCS = $(wildcard $(SRC_DIR)/*.c)
OBJS = $(SRCS:%(SRC_DIR)/%.c=$(OBJS_DIR)/%.o)

CC = cc
CFLAGS = -Wall -Werror -Wextra
GDBFLAG = -g
RM = rm -rf
AR = ar -rcs

TEST = srcs/test_push_swap.c

LIBFTLINK = -L$(LIBFT_DIR) -lft

$(EXEC): $(LIBFTLIB)
	$(CC) $(CFLAGS) $(TEST) $(LIBFTLINK) -o $(EXEC)

$(EXECDEBUG): $(LIBFTLIB)
	$(CC) $(GDBFLAG) $(TEST) $(LIBFTLINK) -o srcs/$(EXECDEBUG)

$(OBJS_DIR)/%.o: %.c | $(OBJS_DIR)
	$(CC) $(CFLAGS) $(GDBFLAG) -c $< -o $@

$(OBJS_DIR):
	mkdir -p $(OBJS_DIR)

$(LIBFTLIB):
	$(MAKE) -C $(LIBFT_DIR) CFLAGS="$(CFLAGS) $(GDBFLAG)"

all: libft $(NAME)

libft: $(LIBFTLIB)

run: libft $(EXEC)
	./$(EXEC)

debug: libft $(EXECDEBUG)
	./srcs/$(EXECDEBUG)

clean:
	$(RM) $(OBJS_DIR)
	$(MAKE) -C $(LIBFT_DIR) clean

fclean: clean
	$(RM) $(NAME) $(EXEC) srcs/$(EXECDEBUG)
	$(MAKE) -C $(LIBFT_DIR) fclean

re: fclean all

.PHONY: all clean fclean re