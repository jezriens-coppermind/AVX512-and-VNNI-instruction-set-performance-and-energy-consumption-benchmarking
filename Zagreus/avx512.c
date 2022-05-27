//Imported libraries
#include <stdlib.h>
#include <immintrin.h>

//Own created libraries
#include "avx512.h"
#include "globals.h"

void execute_avx512() {
    int i, j;
    int reduce;
    float *a, *b;
    __m512 va, vb, vmul, vadd, vdiv;

    //Reserve memory for helpful vectors
    a = (float *) aligned_alloc (64, 64*sizeof (float));
    b = (float *) aligned_alloc (64, 64*sizeof (float));

    //Initialize vectors with random numbers
    srand (1);
    for (int j = 0; j < 64; j++) {
        a[j] = (rand() % 10);
        b[j] = (rand() % 10);
    }

    switch(exec_mode) {
        //Execution mode 1, only a mul command
        case 1:
            for (i = 0; i < command_num; i++) {
                for (j = 0; j < 1000000; j++) {
                    va = _mm512_load_ps(&a[0]);
                    vb = _mm512_load_ps(&b[0]);
                    vmul = _mm512_mul_ps(va, vb);
                }
            }
            break;

        //Execution mode 2, mul and add command
        case 2:
            for (i = 0; i < command_num; i++) {
                for (j = 0; j < 1000000; j++) {
                    vadd = _mm512_setzero_ps();
                    va = _mm512_load_ps(&a[0]);
                    vb = _mm512_load_ps(&b[0]);
                    vmul = _mm512_mul_ps(va, vb);
                    vadd = _mm512_add_ps(vadd, vmul);
                }
            }
            break;

        //Execution mode 3, mul, add and reduce command
        case 3:
            for (i = 0; i < command_num; i++) {
                for (j = 0; j < 1000000; j++) {
                    vadd = _mm512_setzero_ps();
                    va = _mm512_load_ps(&a[0]);
                    vb = _mm512_load_ps(&b[0]);
                    vmul = _mm512_mul_ps(va, vb);
                    vadd = _mm512_add_ps(vadd, vmul);
                    reduce += _mm512_reduce_add_ps(vadd);
                }
            }
            break;

        //Execution mode 4, 3mul, 2add and reduce command
        case 4:
            for (i = 0; i < command_num; i++) {
                for (j = 0; j < 1000000; j++) {
                    vadd = _mm512_setzero_ps();
                    va = _mm512_load_ps(&a[0]);
                    vb = _mm512_load_ps(&b[0]);
                    vmul = _mm512_mul_ps(va, vb);
                    vmul = _mm512_mul_ps(va, vmul);
                    vadd = _mm512_add_ps(vadd, vmul);
                    vmul = _mm512_mul_ps(vadd, vmul);
                    vadd = _mm512_add_ps(va, vmul);
                    reduce += _mm512_reduce_add_ps(vadd);
                }
            }
            break;

        //Execution mode 5, 3mul, 3add, 2div and reduce command
        case 5:
            for (i = 0; i < command_num; i++) {
                for (j = 0; j < 1000000; j++) {
                    vadd = _mm512_setzero_ps();
                    va = _mm512_load_ps(&a[0]);
                    vb = _mm512_load_ps(&b[0]);
                    vmul = _mm512_mul_ps(va, vb);
                    vmul = _mm512_mul_ps(va, vmul);
                    vadd = _mm512_add_ps(vadd, vmul);
                    vmul = _mm512_mul_ps(vadd, vmul);
                    vadd = _mm512_add_ps(va, vmul);
                    vdiv = _mm512_div_ps(vadd, vb);
                    vdiv = _mm512_div_ps(vdiv, va);
                    vadd = _mm512_add_ps(vdiv, vmul);
                    reduce += _mm512_reduce_add_ps(vadd);
                }
            }
            break;
    }

    //Free used memory
    free(a);
    free(b);
}