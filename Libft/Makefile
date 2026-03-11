.DEFAULT_GOAL = re
NAME = a.out
SRC_DIR = attempt_1
OBJS_DIR = $(SRC_DIR)/objs

#SRCS = $(wildcard $(SRC_DIR)/ft_*.c)
SRCS = $(SRC_DIR)/ft_bzero.c
MAIN = main.c
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJS_DIR)/%.o)

CC = cc
CFLAGS = -Wall -Werror -Wextra
RM = rm -rf

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(MAIN) $(OBJS) -o $(NAME)

$(OBJS_DIR)/%.o: $(SRC_DIR)/%.c | $(OBJS_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJS_DIR):
	mkdir -p $(OBJS_DIR)

run: re $(NAME)
	./$(NAME)

clean:
	$(RM) $(OBJS_DIR)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all run clean fclean re