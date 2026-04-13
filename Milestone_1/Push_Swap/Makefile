.DEFAULT_GOAL := all

#COLORS
GREEN = \033[1;92m
RED = \033[1;91m
YELLOW = \033[1;93m
RESET = \033[0m

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
	@$(CC) $(CFLAGS) $(OBJS) $(LIBFTLINK) -o $(NAME)
	@echo "${GREEN}program compiled.${RESET}"

$(DEBUGEXEC): $(OBJS)
	@$(CC) $(GDBFLAG) $(OBJS) $(LIBFTLINK) -o $(DEBUGEXEC)
	@echo "${YELLOW}program compiled with debugger.${RESET}"

$(OBJS_DIR)/%.o: %.c
	@mkdir -p $(dir $@)
	@$(CC) $(CFLAGS) $(GDBFLAG) -c $< -o $@
	@echo "$@ -> ${GREEN}compiled.${RESET}"

$(OBJS_DIR):
	@mkdir -p $(OBJS_DIR)

$(LIBFTLIB):
	@$(MAKE) --no-print-directory -C $(LIBFT_DIR) CFLAGS="$(CFLAGS) $(GDBFLAG)"
	@echo "$@ -> ${GREEN}compiled.${RESET}"

all: libft $(NAME)

debug: libft $(DEBUGEXEC)

libft: $(LIBFTLIB)

clean:
	@$(RM) $(OBJS_DIR)
	@$(MAKE) --no-print-directory -C $(LIBFT_DIR) clean
	@echo "${RED}objects removed.${RESET}"

fclean: clean
	@$(RM) $(NAME) $(DEBUGEXEC)
	@$(MAKE) --no-print-directory -C $(LIBFT_DIR) fclean
	@echo "${RED}program and debugger removed.${RESET}"

re: fclean all

.PHONY: all clean fclean re debug