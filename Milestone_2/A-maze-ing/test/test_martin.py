#!/usr/bin/env python3

# import maze as mz
# from maze_kruskal import Gen_Kruskal
# from maze_solve import Maze_Solve
import src
import random

test_maze = """9139551111555515515395153
ac2a9102829113855692c3a92
814402aac42ac2a9138452a86
a8116aa8552812c0028138683
868696845142a8386846c6942
81294143943a8284529553812
8446943a852c2c4512a95286a
a951292c2f816fffaac296852
8416c2852fc4157f829285452
81453ac56fffafff86aa8153a
84112813913fafd503c2ac102
812a82ac6c2fafffac54692aa
aaaaa8453943c111413956aaa
8682c453c43c3c6c3a82916c2
83ac111451692915286a86956
82c386815416c4292a9685693
829429681141138444294552a
ac69443aa83aa841392c39382
839453a82c46845682812aa82
c44556c6c555455546c446c46"""


def main() -> None:
    m = src.Maze(src.load_maze_config())
    # builder = src.Gen_Kruskal(m)
    # builder.construct(1)
    # print(m.get_print_string())

    m = src.select_gen_algorithm(src.load_maze_config())
    
    print(m.get_print_string())

    # visited_cnt = 0
    # for row in m.cells:
    #     for cell in row:
    #         if cell.visited:
    #             visited_cnt += 1

    # print(visited_cnt)

if __name__ == "__main__":
    main()