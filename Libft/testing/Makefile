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

#Directories of files
SRC_DIR = ../attempt_1
OBJS_DIR = $(SRC_DIR)/objs# Directory used to store generated object files
ROOT_DIR = ~/Desktop/Codam-Core

SRC_FILE = $(wildcard $(SRC_DIR)/ft_*.c)
SRCS = $(SRC_FILE)
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJS_DIR)/%.o)# Map source paths to matching object paths

TEST = $(PARAM)

# Standard build tools and flags
CC = cc
CFLAGS = -Wall -Wextra -Werror
#CFLAGS = -Wall -Wextra -g
#CFLAGS = -Wall -Wextra -lbsd#Use this when working with bsd/string.h functions 
AR = ar rcs
RM = rm -rf

all: $(EXEC)


#-L.  -> search library in current directory
#-lft -> links libft.a
$(EXEC): $(NAME) $(TEST)
	$(CC) $(CFLAGS) $(TEST) -L. -lft -o $(EXEC)


# Build the static library from all compiled object files
$(NAME): $(OBJS)
# `ar` creates an archive file (.a) containing the object files
# `r` replaces existing members in the archive if needed
# `c` creates the archive if it does not already exist
	$(AR) $(NAME) $(OBJS)
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
# Command to run this makefile: make run PARAM='Name of test_file to run' inside test_func/
run: $(EXEC)
	./$(EXEC)

clean:
	$(RM) $(OBJS_DIR)

fclean: clean
	$(RM) $(NAME) $(TEST_DIR)/$(EXEC) $(EXEC) *.dSYM

#Cleans files created when debugging
debugclean: fclean
	$(RM) $(ROOT_DIR)/*.dSYM $(ROOT_DIR)/a.out

# Full rebuild from scratch
re: fclean all

# Declare targets that do not represent real files