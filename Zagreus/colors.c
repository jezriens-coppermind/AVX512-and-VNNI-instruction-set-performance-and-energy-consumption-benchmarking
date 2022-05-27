/*
 * Author: Jon Arriaran
 * This source file sets up color functions for printf and scanf functions
 */
#include <stdio.h>
#include "colors.h"

//Color functions for printf
//No bold colors
void black() { printf("\033[0;30m"); }
void red() { printf("\033[0;31m"); }
void green() { printf("\033[0;32m"); }
void yellow() { printf("\033[0;33m"); }
void blue() { printf("\033[0;34m"); }
void purple() { printf("\033[0;35m"); }
void cyan() { printf("\033[0;36m"); }
void white() { printf("\033[0;37m"); }

//Bold colors
void b_black() { printf("\033[1;30m"); }
void b_red() { printf("\033[1;31m"); }
void b_green() { printf("\033[1;32m"); }
void b_yellow() { printf("\033[1;33m"); }
void b_blue() { printf("\033[1;34m"); }
void b_purple() { printf("\033[1;35m"); }
void b_cyan() { printf("\033[1;36m"); }
void b_white() { printf("\033[1;37m"); }

//reset function
void reset_color() { printf("\033[0m"); }