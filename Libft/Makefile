###
### Build configuration for the test program.
### - Compiles source files from $(SRC_DIR) into object files in $(OBJS_DIR)
### - Archives object files in th static library $(NAME)
### - Links the final executable as $(EXEC)
### - Provides a `run` target to rebuild and execute the program
###

.DEFAULT_GOAL = re# Run `make re` when no target is specified
NAME = libft.a
EXEC = a.out
SRC_DIR = attempt_1
OBJS_DIR = $(SRC_DIR)/objs# Directory used to store generated object files

#SRCS = $(wildcard $(SRC_DIR)/ft_*.c)
SRCS = $(SRC_DIR)/ft_memcpy.c
MAIN = main.c
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJS_DIR)/%.o)# Map source paths to matching object paths

# Standard build tools and flags
CC = cc
CFLAGS = -Wall -Werror -Wextra
RM = rm -rf

all: $(EXEC)


#-L.  -> search library in current directory
#-lft -> links libft.a
$(EXEC): $(NAME) $(OBJS)
	$(CC) $(CFLAGS) $(MAIN) -L. -lft -o $(EXEC)


# Build the static library from all compiled object files
$(NAME): $(OBJS)
# `ar` creates an archive file (.a) containing the object files
# `r` replaces existing members in the archive if needed
# `c` creates the archive if it does not already exist
	ar rc $(NAME) $(OBJS)
# Generate/update the archive index so the linker can find symbols quickly
	ranlib $(NAME)


# Compile each source file into an object file inside $(OBJS_DIR)
# The order-only prerequisite ensures the directory exists without forcing rebuilds
$(OBJS_DIR)/%.o: $(SRC_DIR)/%.c | $(OBJS_DIR)
	$(CC) $(CFLAGS) -c $< -o $@


# Create the object directory only if it does not already exist
$(OBJS_DIR):
	mkdir -p $(OBJS_DIR)


# Rebuild everything, then run the executable
run: re $(EXEC)
	./$(EXEC)

clean:
	$(RM) $(OBJS_DIR)

fclean: clean
	$(RM) $(NAME) $(EXEC)

# Full rebuild from scratch
re: fclean all

# Declare targets that do not represent real files
.PHONY: all run clean fclean re