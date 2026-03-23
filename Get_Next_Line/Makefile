###
### Build configuration for get_next_line
### 
###

EXEC = a.out

OBJS_DIR = objs

SRCS = $(wildcard *.c)
OBJS = $(SRCS:%.c=$(OBJS_DIR)/%.o)

CC = cc
CFLAGS = -Wall -Werror -Wextra -D
CFLAGS = -Wall -Werror -Wextra -g#Debug
RM = rm -rf
PARAM = 4096

all: $(EXEC)

$(EXEC):
#$(CC) $(CFLAGS) BUFFER_SIZE=$(PARAM) $(SRCS) -o $(EXEC)
	$(CC) $(CFLAGS) $(SRCS) -o $(EXEC)

$(OBJS_DIR)/%.o: %.c | $(OBJS_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJS_DIR):
	mkdir -p $(OBJS_DIR)

clean:
	$(RM) $(OBJS_DIR)

fclean: clean
	$(RM) $(EXEC)

re: fclean all

.PHONY: all clean fclean re