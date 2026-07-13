# A-Maze-ing: Maze Generator Project Overview

## Executive Summary

The A-Maze-ing project requires developing a Python 3.10+ maze generator that reads a configuration file, generates a maze using a specified algorithm, encodes the result in hexadecimal wall representation, and displays it visually. The project must produce a reusable, pip-installable Python module alongside a main executable program. Both perfect (single path) and imperfect mazes are supported.

**Key Deliverables:**
- Executable Python program (`a_maze_ing.py`)
- Configuration file parser and validator
- Maze generation engine with seed reproducibility
- Hexadecimal wall encoding (one hex digit per cell)
- Visual rendering (ASCII terminal and/or MLX graphical)
- Solution path finder (BFS/DFS from entry to exit)
- Reusable pip-installable package
- Comprehensive README and documentation

---

## Project Goals

1. Implement a randomized maze generation algorithm with seed reproducibility
2. Encode maze structure as hexadecimal wall data (one hex digit per cell)
3. Provide both ASCII terminal and graphical (MLX) visual representation
4. Output maze data and solution path to a file in specified format
5. Create a reusable, installable Python package for maze generation
6. Document the project thoroughly for peer understanding and recruitment value

---

## Mandatory Technical Requirements

### Configuration File Format

The program accepts a configuration file with the following **mandatory** fields:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `WIDTH` | Integer | Number of maze cells horizontally | `WIDTH=20` |
| `HEIGHT` | Integer | Number of maze cells vertically | `HEIGHT=15` |
| `ENTRY` | Tuple (x,y) | Entry point coordinates | `ENTRY=0,0` |
| `EXIT` | Tuple (x,y) | Exit point coordinates | `EXIT=19,14` |
| `OUTPUT_FILE` | String | Output filename | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | Boolean | Perfect maze (single path) or not | `PERFECT=True` |

**Optional fields:** `SEED` (reproducibility), `ALGORITHM` (generation method choice), `DISPLAY_MODE` (rendering preference)

**Rules:**
- Format: `KEY=VALUE`, one pair per line
- Lines starting with `#` are comments and must be ignored
- Default configuration file must be available in Git repository

---

### Maze Structure and Validity Rules

| Requirement | Details |
|-------------|---------|
| **Cell Walls** | Each cell contains 0–4 walls at cardinal directions (N, E, S, W) |
| **Entry/Exit** | Must exist, be different, and reside within maze bounds |
| **Connectivity** | Full connectivity with no isolated cells (except "42" pattern) |
| **External Borders** | All boundary cells have walls on edges |
| **Wall Coherence** | If cell A has an east wall, the cell to the east must have a west wall |
| **Corridor Width** | No corridors wider than 2 cells (no 3×3 open areas; 2×3 or 3×2 allowed) |
| **Perfect Mode** | When `PERFECT=True`, exactly one valid path must exist between entry and exit |
| **"42" Pattern** | Maze must display a visible "42" made of fully closed cells when rendered (omit only if maze too small; print error message) |

---

### Hexadecimal Wall Encoding

Each cell is encoded as one hexadecimal digit, where each bit represents a wall direction:

| Bit | Value | Direction | Meaning |
|-----|-------|-----------|---------|
| 0 (LSB) | 1 | North | Bit set to 1 = wall present; 0 = wall absent |
| 1 | 2 | East | Bit set to 1 = wall present; 0 = wall absent |
| 2 | 4 | South | Bit set to 1 = wall present; 0 = wall absent |
| 3 | 8 | West | Bit set to 1 = wall present; 0 = wall absent |

**Examples:**
- `0x3` (binary `0011`) → South and West walls open, North and East closed
- `0xA` (binary `1010`) → East and West walls closed, North and South open
- `0xF` (binary `1111`) → All four walls closed (isolated cell)
- `0x0` (binary `0000`) → All walls open (fully connected cell)

**Output Format:**
- Cells stored row by row
- One row per line
- Each cell as one hexadecimal digit (0–F)

---

### Output File Format

```
<hex_row_1>
<hex_row_2>
...
<hex_row_n>

<entry_x>,<entry_y>
<exit_x>,<exit_y>
<path_sequence>
```

| Component | Description | Format | Example |
|-----------|-------------|--------|---------|
| Hex Maze Data | All cells encoded as hexadecimal | Rows separated by `\n` | `9151515315...` |
| Empty Line | Separates maze from metadata | Single `\n` | — |
| Entry | Entry point coordinates | `x,y` | `0,0` |
| Exit | Exit point coordinates | `x,y` | `19,14` |
| Path Sequence | Shortest path from entry to exit | Cardinal letters: N, E, S, W | `SWSESEWSESESSSS...` |
| Line Endings | All lines must end with newline | `\n` | — |

---

### Visual Representation Requirements

The program must display the maze using **one of two methods:**

#### 1. Terminal ASCII Rendering
- Use text characters (e.g., `█`, `─`, `│`, corners) to show walls
- Clearly mark entry and exit
- Optionally show solution path with distinct character or color
- Support toggling path display on/off

#### 2. MiniLibX (MLX) Graphical Display
- Render maze as grid with wall segments
- Use colors to distinguish walls, paths, entry, exit
- Display entry and exit markers
- Handle window close and interaction properly

#### User Interaction Requirements
All implementations must support at least:

| Interaction | Purpose |
|-------------|---------|
| Regenerate maze | Generate new maze with same or new random seed, display immediately |
| Show/Hide path | Toggle display of shortest path from entry to exit |
| Change wall colors | Modify wall appearance color |
| 42 Pattern color (optional) | Set specific colors for the "42" pattern |

Additional interactions are permitted and encouraged.

---

## Code Reusability and Packaging

### Reusable Module Requirements

| Requirement | Details |
|-------------|---------|
| **Class Name** | Encapsulate logic in single class (e.g., `MazeGenerator`) |
| **Module Location** | Standalone module importable by other projects |
| **Public Interface** | Expose: instantiation, custom parameters, generated structure, solution path |
| **Structure Format** | Internal representation need not match hexadecimal output file format |
| **Documentation** | Include short doc with examples, parameter options, and access methods |

### Pip-Installable Package

| Requirement | Specification |
|-------------|---------------|
| **Package Name** | Must begin with `mazegen-` (e.g., `mazegen-1.0.0`) |
| **Formats** | Distribute as `.tar.gz` or `.whl` (wheel) |
| **Location** | Root of Git repository |
| **Example Filename** | `mazegen-1.0.0-py3-none-any.whl` |
| **Build Files** | Include `setup.py` and/or `pyproject.toml` |
| **Testability** | Must install and build in fresh virtual environment during evaluation |

### Package Documentation

Provide documentation covering:

1. **Instantiation and Usage**
   - Basic example of creating a MazeGenerator instance
   - Minimal working code snippet

2. **Custom Parameters**
   - How to set maze size
   - How to provide or use a seed
   - How to select algorithm (if multiple available)

3. **Accessing Results**
   - How to retrieve generated maze structure
   - How to obtain solution path
   - Any other relevant public methods

---

## Detailed Task Breakdown

### Phase 1: Planning and Design (Foundation)

| Task ID | Task Name | Objective | Details | Est. Duration | Deliverable |
|---------|-----------|-----------|---------|----------------|-------------|
| 1.1 | Configuration Parser | Read and validate config files | Parse KEY=VALUE pairs, ignore comments, validate mandatory fields, enforce data types and bounds, provide clear error messages | 1–2 days | Validated config object |
| 1.2 | Maze Data Structure | Design internal representation | Decide on 2D array, cell objects, or adjacency lists; define wall storage; plan solution tracking | 1 day (design) | Class and data structure specs |
| 1.3 | Algorithm Research | Choose generation algorithm(s) | Evaluate Recursive Backtracker, Kruskal's, Prim's, Eller's for suitability with perfect/imperfect, seed reproducibility, performance | 2–3 days | Algorithm specification and pseudocode |

### Phase 2: Core Maze Generation (Main Logic)

| Task ID | Task Name | Objective | Details | Est. Duration | Deliverable |
|---------|-----------|-----------|---------|----------------|-------------|
| 2.1 | Implement Algorithm | Write generation algorithm | Implement chosen algorithm with seed support, ensure wall coherence, prevent isolated cells, enforce corridor width, generate "42" pattern, respect entry/exit | 5–7 days | Working MazeGenerator class |
| 2.2 | Perfect Maze Mode | Guarantee single path | Modify algorithm or add verification to ensure exactly one path when PERFECT=True | 2–3 days | Verified perfect maze generation |
| 2.3 | Solution Path Finder | Calculate entry-to-exit path | Implement BFS or DFS, convert to cardinal letters (N/E/S/W) | 2 days | Path finding function |

### Phase 3: Output and Encoding (Data Serialization)

| Task ID | Task Name | Objective | Details | Est. Duration | Deliverable |
|---------|-----------|-----------|---------|----------------|-------------|
| 3.1 | Hexadecimal Encoding | Convert maze to hex representation | For each cell, encode four wall bits as single hex digit; output one hex per cell; write one row per line | 1 day | Hex encoding module |
| 3.2 | Output File Writing | Write complete output file | Write hex maze, blank line, entry, exit, path; ensure all lines end with `\n`; validate format | 1 day | File writing function |

### Phase 4: Visualization (Display)

| Task ID | Task Name | Objective | Details | Est. Duration | Deliverable |
|---------|-----------|-----------|---------|----------------|-------------|
| 4.1 | ASCII Terminal Renderer | Display maze in terminal | Use box drawing characters or symbols for walls; mark entry/exit; optionally show path; support color output | 3–4 days | ASCII renderer with path toggle |
| 4.2 | MLX Graphical Renderer | Display maze with graphics library | Render grid with wall segments; color walls and paths; display markers; handle window/interaction | 5–7 days | MLX renderer with interaction |
| 4.3 | User Interaction Menu | Implement interactive controls | Handle regeneration, path toggle, color change; provide on-screen menu or instructions | 2–3 days | Functional menu system |

### Phase 5: Code Packaging (Reusability)

| Task ID | Task Name | Objective | Details | Est. Duration | Deliverable |
|---------|-----------|-----------|---------|----------------|-------------|
| 5.1 | Create Reusable Module | Extract generation into importable package | Isolate MazeGenerator class; remove display code; make importable; write module documentation | 2 days | Standalone module with docs |
| 5.2 | Create Pip Package | Package as distributable Python module | Create setup.py/pyproject.toml; build .whl or .tar.gz; test in fresh venv | 1–2 days | mazegen-X.X.X package |

### Phase 6: Documentation and Testing (Polish)

| Task ID | Task Name | Objective | Details | Est. Duration | Deliverable |
|---------|-----------|-----------|---------|----------------|-------------|
| 6.1 | Write README.md | Comprehensive project documentation | Include all mandatory sections, algorithm explanation, team roles, planning evolution, tool usage | 2–3 days | Complete README file |
| 6.2 | Config Validation Testing | Verify parser robustness | Test valid/invalid inputs, missing fields, type errors, boundary conditions | 1 day | Test cases and validation report |
| 6.3 | Maze Generation Testing | Verify maze correctness | Check wall coherence, connectivity, "42" pattern, perfect mode guarantee, seed reproducibility, corridor width | 2–3 days | Test suite and verification report |
| 6.4 | Output File Validation | Verify output format | Check hex encoding, entry/exit, path validity; use provided validation script | 1 day | Validated output files |

---

## Suggested Task Division for Two Partners

### Partner A: Algorithm & Core Engine
**Ownership:** Maze generation logic, encoding, reusable module internals

| Task | Phase | Duration |
|------|-------|----------|
| 1.2 – Maze Data Structure | 1 | 1 day |
| 1.3 – Algorithm Research | 1 | 2–3 days |
| 2.1 – Implement Algorithm | 2 | 5–7 days |
| 2.2 – Perfect Maze Mode | 2 | 2–3 days |
| 2.3 – Solution Path Finder | 2 | 2 days |
| 3.1 – Hexadecimal Encoding | 3 | 1 day |
| 5.1 – Create Reusable Module | 5 | 2 days |
| 6.3 – Maze Testing | 6 | 2–3 days |

**Total Estimated: 18–24 days** (concurrent, not sequential)

**Primary Responsibilities:**
- Design the internal maze data structure
- Research and select the generation algorithm
- Implement the complete generation engine
- Ensure mathematical correctness (connectivity, wall coherence, etc.)
- Create the reusable package module
- Write technical tests for maze validity

---

### Partner B: Configuration, Visualization & Documentation
**Ownership:** User interface, file I/O, visual rendering, documentation

| Task | Phase | Duration |
|------|-------|----------|
| 1.1 – Configuration Parser | 1 | 1–2 days |
| 3.2 – Output File Writing | 3 | 1 day |
| 4.1 – ASCII Terminal Renderer | 4 | 3–4 days |
| 4.2 – MLX Graphical Renderer | 4 | 5–7 days |
| 4.3 – User Interaction Menu | 4 | 2–3 days |
| 5.2 – Create Pip Package | 5 | 1–2 days |
| 6.1 – Write README | 6 | 2–3 days |
| 6.2 – Config Testing | 6 | 1 day |
| 6.4 – Output Validation | 6 | 1 day |

**Total Estimated: 17–27 days** (concurrent, not sequential)

**Primary Responsibilities:**
- Parse and validate configuration files robustly
- Handle all file I/O and error messages
- Implement visual rendering (ASCII and/or MLX)
- Create interactive menu system
- Write and test the pip package build process
- Create comprehensive documentation and README
- Perform configuration and output validation testing

---

### Collaborative / Integration Tasks

| Task | Participants | Notes |
|------|--------------|-------|
| 1.1 – Config Parser | Both | Partner B implements; Partner A reviews for integration needs |
| Planning sync | Both | Agree on data structure interfaces before coding |
| Code review | Both | Pull requests before merge to develop branch |
| Phase 6 testing | Both | Partner A tests maze validity; Partner B tests UI/I/O |
| Final integration | Both | Ensure all components work together; final validation |

---

## Git Workflow and Collaboration

### Repository Structure

```
a-maze-ing/
├── a_maze_ing.py              # Main executable
├── config.txt                  # Default configuration
├── README.md                   # Project documentation
├── Makefile                    # Build automation
├── pyproject.toml              # Python package config
├── setup.py                    # Package setup (alternative)
├── .gitignore                  # Python artifacts
├── src/
│   ├── maze_generator.py       # Core maze generation (Partner A)
│   ├── config_parser.py        # Configuration handling (Partner B)
│   ├── output_writer.py        # File output (Partner B)
│   ├── renderer/
│   │   ├── ascii_renderer.py   # ASCII display (Partner B)
│   │   └── mlx_renderer.py     # MLX display (Partner B)
│   └── utils/
│       ├── pathfinding.py      # Path calculation (Partner A)
│       └── validation.py       # Maze validation (Partner A)
├── mazegen/                    # Reusable module (from src/)
│   ├── __init__.py
│   └── maze_generator.py       # Core class for pip package
└── tests/                      # Test suite (both)
    ├── test_config.py
    ├── test_maze_generation.py
    ├── test_output.py
    └── test_rendering.py
```

### Branching Strategy

```
main                           (stable, final submission)
  └── develop                  (integration branch)
      ├── generation/core      (Partner A: algorithm, encoding)
      ├── generation/pathfind  (Partner A: path finding)
      ├── ui/config            (Partner B: config parser)
      ├── ui/renderer-ascii    (Partner B: ASCII rendering)
      ├── ui/renderer-mlx      (Partner B: MLX rendering)
      ├── docs/readme          (Partner B: documentation)
      └── packaging/pip        (Partner B: pip package)
```

### Workflow

1. Each partner creates feature branches from `develop`
2. Work independently on assigned tasks
3. Create pull request (PR) when feature complete
4. Partner reviews code for correctness and integration
5. Merge to `develop` after approval
6. Regular (daily or every 2 days) integration sync to catch conflicts early
7. Final integration PR from `develop` to `main` before submission

---

## Critical Constraints and Edge Cases

### Python Standards

| Requirement | Details |
|-------------|---------|
| **Python Version** | 3.10 or later (mandatory) |
| **Type Hints** | Required for all functions and variables; use `typing` module |
| **Type Checking** | All code must pass `mypy` without errors |
| **Code Style** | Flake8 compliance (mandatory) |
| **Docstrings** | PEP 257 required (Google or NumPy style) |
| **Exception Handling** | All exceptions must be caught; no unhandled crashes |
| **Resource Management** | Use context managers for files and connections |

### Validation and Error Handling

| Scenario | Expected Behavior |
|----------|-------------------|
| Config file missing | Clear error message, exit gracefully |
| Malformed config (bad syntax) | Parse error with line number, helpful message |
| Missing mandatory field | Error listing which field(s) required |
| Invalid data type | Type error with expected type shown |
| Entry/Exit out of bounds | Rejection with bounds check explanation |
| Entry equals exit | Rejection with explanation |
| Maze too small for "42" pattern | Error message printed to console (allowed omission) |
| Seed invalid or missing | Default to system random or fail gracefully |
| File I/O error | Catch, log, and provide user-friendly message |
| Impossible maze parameters | Error message (e.g., 1×1 maze, seed conflicts) |

### Makefile Rules (Mandatory)

```makefile
install:      # Install project dependencies
run:          # Execute a_maze_ing.py with default config
debug:        # Run with Python debugger (pdb)
clean:        # Remove __pycache__, .mypy_cache, etc.
lint:         # Run flake8 and mypy with standard flags
lint-strict:  # Run mypy with --strict flag (optional)
```

---

## Deliverables Checklist

### Core Implementation
- [ ] Working `a_maze_ing.py` executable program
- [ ] Valid default configuration file included in repository
- [ ] Configuration parser (robust, with full error handling)
- [ ] Maze generation engine (with seed reproducibility)
- [ ] Perfect maze mode implementation
- [ ] Hexadecimal wall encoding module
- [ ] Solution path finding (BFS/DFS)
- [ ] File output writer (correct format with `\n` line endings)

### Visualization
- [ ] ASCII terminal rendering with path toggle
- [ ] MLX graphical rendering (recommended) or enhanced ASCII
- [ ] User interaction menu (regenerate, toggle path, change colors)
- [ ] "42" pattern visible in rendered output

### Packaging & Reusability
- [ ] Reusable `MazeGenerator` class in standalone module
- [ ] Pip-installable package: `mazegen-X.X.X.whl` or `.tar.gz`
- [ ] `setup.py` or `pyproject.toml` for building package
- [ ] Module documentation with examples
- [ ] Package installs and builds in fresh virtual environment

### Documentation
- [ ] Complete `README.md` with all mandatory sections
- [ ] Algorithm explanation and rationale
- [ ] Team roles and project management notes
- [ ] AI tool usage explicitly described
- [ ] Configuration file format documented
- [ ] Code reusability section with examples

### Code Quality
- [ ] Type hints on all functions and variables
- [ ] Passes `mypy` without errors (ideally `--strict`)
- [ ] Passes `flake8` checks
- [ ] PEP 257 docstrings on all functions/classes
- [ ] Exception handling throughout (no unhandled crashes)
- [ ] `.gitignore` includes Python artifacts

### Testing & Validation
- [ ] Configuration parser validation tests
- [ ] Maze generation validation tests (coherence, connectivity)
- [ ] Output file format validation tests
- [ ] Perfect maze verification (one path guaranteed)
- [ ] Seed reproducibility tests
- [ ] Visual rendering smoke tests

### Git & Submission
- [ ] Clean commit history with meaningful messages
- [ ] All code in Git repository
- [ ] Branch strategy followed (main/develop/feature)
- [ ] No large binary files or unnecessary artifacts
- [ ] README visible at repository root

---

## Timeline Estimate

Assuming concurrent work with regular collaboration and minimal blocking:

| Phase | Activity | Duration | Notes |
|-------|----------|----------|-------|
| 1 | Planning, design, algorithm research | 3–4 days | Both partners discuss, decide together |
| 2–4 | Core development (generation, rendering, paths) | 15–20 days | Parallel work; daily integration syncs |
| 5 | Packaging and module extraction | 3–4 days | Can overlap with Phase 4 end |
| 6 | Testing, validation, documentation | 4–5 days | Both partners; write during development |
| — | **Total Calendar Duration** | **25–33 days** | **Concurrent; not sequential** |

**Key Assumptions:**
- Both partners working simultaneously
- Regular (daily or every 2 days) sync meetings to catch integration issues early
- No major blocking dependencies (well-defined interfaces)
- Testing done incrementally, not at the end

---

## Next Steps

### Immediate Actions (Day 1–2)

1. **Review this task breakdown together** (both partners)
   - Discuss task sizes and effort estimates
   - Identify any missing or unclear tasks

2. **Clarify roles and responsibilities**
   - Confirm Partner A and Partner B assignments
   - Discuss ownership boundaries (who owns what code)

3. **Select maze generation algorithm**
   - Research Recursive Backtracker, Kruskal's, Prim's, Eller's
   - Decide based on suitability, complexity, seed reproducibility
   - Document rationale in planning notes

4. **Define data structure interfaces**
   - Agree on how Partner A will expose maze structure to Partner B
   - Plan configuration object format that Partner B produces
   - Plan path format (list of cardinal letters)

5. **Establish Git workflow**
   - Create GitHub repository (shared collaboration)
   - Define branch naming conventions
   - Set up `.gitignore`, initial directory structure
   - Create initial commits

6. **Set up development environment**
   - Python 3.10+ with venv or conda
   - Install: `flake8`, `mypy`, `pytest`
   - Makefile ready for `install`, `lint`, `run`

7. **Create initial repository structure**
   - Scaffold directories (src/, mazegen/, tests/)
   - Create placeholder files with docstring stubs
   - Commit initial structure

### Week 1 (Implementation Start)

- **Partner A:** Begin data structure design and algorithm research
- **Partner B:** Begin configuration parser implementation
- **Both:** Daily 15-minute sync on blockers, integration points

### Ongoing

- Code reviews on all PRs
- Weekly longer sync for planning adjustments
- Test as you go, don't wait until end
- Document decisions in commit messages and code comments

---

## Summary

This project is a medium-complexity Python application combining algorithmic thinking (maze generation, pathfinding), file I/O, visual rendering, and packaging. Success depends on clear separation of concerns, early agreement on interfaces, and consistent integration testing. The suggested division leverages each partner's strengths: algorithm and mathematics (Partner A) vs. user interface and system integration (Partner B).

Good luck, and happy coding!