.ONESHELL:

.DEFAULT_GOAL := help

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

# ------------------ Paths  ------------------ #
FUNC_DEF			:= data/input/functions_definition.json
INPUT				:= data/input/function_calling_tests.json
OUTPUT				:= data/output/function_calls.json

# ------------------ Tools  ------------------ #
VENV				:= .venv
UV					:= ${VENV}/bin/uv
RUN_COMM			:= ${UV} run python

MYPY_FLAGS			:= . --warn-return-any --warn-unused-ignores \
						--ignore-missing-imports --disallow-untyped-defs \
						--check-untyped-defs --explicit-package-bases

MYPY_STRICT_FLAGS	:= . --strict --explicit-package-bases

STD_ARGS			:= --functions_definition ${FUNC_DEF} \
					   --input ${INPUT} \
					   --output ${OUTPUT}

$(VENV):
	@echo "${YELLOW}Creating virtual environment...${RESET}"
	@uv venv  --prompt Call_Me_Maybe > /dev/null 2>&1

	@echo "${CYAN}	RUN 'source ./env/bin/activate \
	('activate.fish' if using fish)${RESET}"

# ------------------ Commands ------------------ #
help:
	@echo "${BOLD}Available commands:${RESET}"
	@echo "${CYAN}  make install${RESET}     - Create venv and install dependencies with uv"
	@echo "${CYAN}  make run${RESET}        - Run the program"
	@echo "${CYAN}  make debug${RESET}      - Run with debugger (pdb by default)"
	@echo "${CYAN}  make lint${RESET}       - Run flake8 and mypy"
	@echo "${CYAN}  make lint-strict${RESET} - Run flake8 and mypy --strict"
	@echo "${CYAN}  make clean${RESET}      - Remove cache folders"
	@echo "${CYAN}  make fclean${RESET}     - Remove venv and cache"

install: $(VENV)
	@echo "${YELLOW}Installing dependencies...${RESET}"
	uv sync --link-mode=copy

	@echo "${GREEN}\nEverything installed ${RESET}"

run: install
	@echo "${GREEN}\nRunning... !!${RESET}"
	@ ${RUN_COMM} -m src ${STD_ARGS}

# debug: $(VENV) install
# 	@echo "${PURPLE}Running $(PROG) in debug mode with $(DEBUGGER)...${RESET}"
# 	@$(PYTHON) -m pdb $(PROG) $(CONFIG) 2>/dev/null

clean:
	@echo "${RED}Removing '.mypy_cache' folders.${RESET}"
	@find . -type d -name .mypy_cache -exec rm -rf {} +

	@echo "${RED}Removing '__pycache__' folders.${RESET}"
	@find . -type d -name __pycache__ -exec rm -rf {} +

	@echo "${RED}Removing '.pyc' files.${RESET}"
	@find . -type f -name "*.pyc" -exec rm -rf {} +

fclean: clean
	@echo "${RED}Removing '.venv'.${RESET}"
	@rm -rf $(VENV)


	@echo "${YELLOW}\nMAKE SURE YOU EXIT VENV 'deactivate'.${RESET}"

lint:
	@echo "${YELLOW}Running flake8...${RESET}"
	-@flake8 . && echo "${GREEN}✓ flake8 passed${RESET}" || true

	@echo "${YELLOW}\nRunning mypy...${RESET}"
	-@mypy ${MYPY_FLAGS} && echo "${GREEN}✓ mypy passed${RESET}" || true

lint-strict:
	@echo "${YELLOW}Running flake8...${RESET}"
	@flake8 . && echo "${GREEN}✓ flake8 passed${RESET}" || true

	@echo "${YELLOW}Running mypy --strict...${RESET}"
	@mypy ${MYPY_STRICT_FLAGS} && echo "${GREEN}✓ mypy --strict passed${RESET}"|| true

.PHONY: install wheel run debug clean fclean lint lint-strict help deactivate_env