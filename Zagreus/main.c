//Imported libraries
#include <stdio.h>
#include <stdlib.h>
#include <immintrin.h>
#include <time.h>

//Own created libraries
#include "avx512_vnni.h"
#include "avx512.h"
#include "colors.h"

//Program main function variables
int command_num = 0, m512_size = 0, mode = 0, exec_mode = 0;
__m512i src, a, b;

int main(int argc, char *argv[]) {

    //Variables for time taking
    double tex;
    struct timespec  t0, t1;

    if (argc == 5) {

        //Get parameters
        //---------------------------------------------------------------
        mode = atoi(argv[1]);
        command_num = atoi(argv[2]);
        m512_size = atoi(argv[3]);
        exec_mode = atoi(argv[4]);
        //---------------------------------------------------------------


        //Detection of errors on arguments
        //---------------------------------------------------------------
        //b_red(); //Color Change
        if (mode <= 0 || mode > 3) {
            fprintf(stderr, "Error on mode selection \n"
                            "Argument has to be between 1-3 \n");
            return 1;
        }
        else if (command_num <= 0) {
            fprintf(stderr, "Error on command_num selection \n"
                            "Argument has to be higher than 0 \n");
            return 1;
        }
        else if (m512_size <= 0) {
            fprintf(stderr, "Error on vectors sizes selection \n"
                            "Argument has to be higher than 0 \n");
            return 1;
        }
        else if (exec_mode <= 0 || exec_mode > 5) {
            fprintf(stderr, "Error on execution mode selection \n"
                            "Argument has to be between 0 and 5 \n");
            return 1;
        }
        //---------------------------------------------------------------

        //Execution of different modes & time take
        //---------------------------------------------------------------
        if (mode == 1) {
            clock_gettime (CLOCK_REALTIME, &t0);
            execute_avx512();
            clock_gettime (CLOCK_REALTIME, &t1);
            tex = (t1.tv_sec - t0.tv_sec) + (t1.tv_nsec - t0.tv_nsec) / (double)1e9;

            //Print elapsed time
            //b_yellow(); printf("\nElapsed time: ");
            printf("%.2fs \n", tex);
        }

        if (mode == 2) {
            clock_gettime (CLOCK_REALTIME, &t0);
            initialize_avx512();
            clock_gettime (CLOCK_REALTIME, &t1);
            tex = (t1.tv_sec - t0.tv_sec) + (t1.tv_nsec - t0.tv_nsec) / (double)1e9;

            //Print elapsed time
            //b_yellow(); printf("\nElapsed time: ");
            printf("%.2fs \n", tex);
        }
        //---------------------------------------------------------------
    }
    else {
        b_red(); //Color Change
        fprintf(stderr, "Error on arguments \n"
                        "You need to put 4 arguments on the command \n");
        return 1;
    }

    return 0;
}
