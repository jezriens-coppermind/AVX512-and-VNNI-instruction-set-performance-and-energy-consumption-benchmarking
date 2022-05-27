#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <immintrin.h>

#include "avx512_vnni.h"
#include "globals.h"

void initialize_avx512() {

    //Private helpful variables declaration
    int i, j;
    srand(1);
    __m512i src, result, A, B;
    int a = (rand() % 10) + 1;
    int b = (rand() % 10) + 1;
    int c = (rand() % 10) + 1;

    uint64_t arr_a[512 / m512_size];
    uint64_t arr_b[512 / m512_size];
    uint64_t arr_src[512 / m512_size];
    for (int j = 0; j < 512 / m512_size; j++) {
        switch (m512_size) {
            case 64:
                arr_a[j] = (uint64_t) a;
                arr_b[j] = (uint64_t) b;
                arr_src[j] = (uint64_t) c;
                break;

            case 32:
                arr_a[j] = (uint32_t) a;
                arr_b[j] = (uint32_t) b;
                arr_src[j] = (uint32_t) c;
                break;

            case 16:
                arr_a[j] = (uint16_t) a;
                arr_b[j] = (uint16_t) b;
                arr_src[j] = (uint16_t) c;
                break;

            case 8:
                arr_a[j] = (uint8_t) a;
                arr_b[j] = (uint8_t) b;
                arr_src[j] = (uint8_t) c;
                break;
        }
    }

    A = _mm512_loadu_si512((__m512i * ) & arr_a);
    B = _mm512_loadu_si512((__m512i * ) & arr_b);
    src = _mm512_loadu_si512((__m512i * ) & arr_src);

    switch (exec_mode) {
        case 1:
            for (i = 0; i < command_num; i++) {
                for (j = 0; j < 1000000; j++) {
                    result = _mm512_dpbusd_epi32(src, A, B);
                }
            }
            break;

        case 2:
            for (i = 0; i < command_num; i++) {
                for (j = 0; j < 1000000; j++) {
                    result = _mm512_dpbusds_epi32(src, A, B);
                }
            }
            break;

        case 3:
            for (i = 0; i < command_num; i++) {
                for (j = 0; j < 1000000; j++) {
                    result = _mm512_dpwssd_epi32(src, A, B);
                }
            }
            break;

        case 4:
            for (i = 0; i < command_num; i++) {
                for (j = 0; j < 1000000; j++) {
                    result = _mm512_dpwssds_epi32(src, A, B);
                }
            }
            break;

	case 5:
            for (i = 0; i < command_num; i++) {
                for (j = 0; j < 1000000; j++) {
                    int command;
                    command = rand() % 4;
                    switch (command) {
                        case 0:
                            result = _mm512_dpbusd_epi32(src, A, B);
                            break;

                        case 1:
                            result = _mm512_dpbusds_epi32(src, A, B);
                            break;

                        case 2:
                            result = _mm512_dpwssd_epi32(src, A, B);
                            break;

                        case 3:
                            result = _mm512_dpwssds_epi32(src, A, B);
                            break;
                    }
                }
            }
            break;

    }
}
