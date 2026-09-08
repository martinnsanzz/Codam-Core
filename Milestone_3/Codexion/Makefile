.ONESHELL:

.DEFAULT_GOAL := all

# ------------------ Colors ------------------ #
GREEN				:= \033[1;92m
RED					:= \033[1;91m
YELLOW				:= \033[1;93m
RESET				:= \033[0m
PURPLE				:= \033[95m
BLUE				:= \033[94m
CYAN				:= \033[96m
BOLD				:= \033[1m
UNDERLINE			:= \033[4m


# ------------------ Tools ------------------ #
CC					:= cc
C_FLAGS				:= -Wall -Werror -Wextra
GDB_FLAG			:= -g
LPTHREAD_FLAG		:= -lpthread
RM					:= rm -rf


# ---------- Program Requirements ---------- #
NAME				:= codexion
DEBUGEXEC			:= a.out.debug

OBJS_DIR			:= objs
OBJS_DIR_DEBUG		:= objs_debug

SRCS				:= codexion.c \
						validation.c \
						utils.c

OBJS				:= $(SRCS:%.c=$(OBJS_DIR)/%.o)
OBJS_DEBUG			:= $(SRCS:%.c=$(OBJS_DIR_DEBUG)/%.o)


# --------------- Recipes --------------- #
$(NAME): $(OBJS)
	@echo "${YELLOW}Compiling program...\n${RESET}"
	@$(CC) $(C_FLAGS) $(OBJS) $(LPTHREAD_FLAG) -o $(NAME)

$(OBJS_DIR):
	@mkdir -p $(OBJS_DIR)

$(OBJS_DIR)/%.o: %.c | $(OBJS_DIR)
	@$(CC) $(C_FLAGS) -c $< -o $@


# ------------ Debug Recipes ------------ #
$(DEBUGEXEC): $(OBJS_DEBUG)
	@echo "${PURPLE}Compiling program in debug mode...\n${RESET}"
	@$(CC) $(GDB_FLAG) $(OBJS_DEBUG) $(LPTHREAD_FLAG) -o $(DEBUGEXEC)

$(OBJS_DIR_DEBUG):
	@mkdir -p $(OBJS_DIR_DEBUG)

$(OBJS_DIR_DEBUG)/%.o: %.c | $(OBJS_DIR_DEBUG)
	@$(CC) $(GDB_FLAG) -c $< -o $@


# ------------------ Commands ------------------ #
help:
	@echo "${BOLD}Available commands:${RESET}"
	@echo "${CYAN}  make clean${RESET}      - Remove cache folders"
	@echo "${CYAN}  make fclean${RESET}     - Remove venv and cache"

help-run:
	@echo "${CYAN}To run the program the following arguments must be passed:${RESET}\n"

	@echo "${BOLD}./codexion 1:'number_of_coders' 2:'time_to_burnout (in milliseconds)' \
3:'time_to_compile (in milliseconds)' 4:'time_to_debug (in milliseconds)' \
5:'time_to_refactor (in milliseconds)' 6:'number_of_compiles_required' \
7:'dongle_cooldown (in milliseconds)' 8:'scheduler (fifo or edf)'${RESET}\n"

	@echo "${YELLOW} For more information go to subject.pdf page 8."

all: $(NAME)
	@echo "${GREEN}Program is compiled and ready to use !! $(DEBUGGER)...${RESET}"
	@echo "${BOLD}	Run ./$(NAME) $(DEBUGGER)...${RESET}"

debug: $(DEBUGEXEC)
	@echo "${GREEN}Debug program is compiled and ready to use !! $(DEBUGGER)...${RESET}"

clean:
	@echo "${RED}Removing '$(OBJS_DIR)' folder.${RESET}"
	@$(RM) $(OBJS_DIR)

	@echo "${RED}Removing '$(OBJS_DIR_DEBUG)' folder.${RESET}"
	@$(RM) $(OBJS_DIR_DEBUG)


fclean: clean
	@echo "${RED}Removing '$(NAME)' program.\n${RESET}"
	@$(RM) $(NAME)

	@echo "${RED}Removing '$(DEBUGEXEC)' file.${RESET}"
	@$(RM) $(DEBUGEXEC)

re: fclean all debug

.PHONY: help help-run all debuf clean fclean re