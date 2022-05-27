#!/bin/bash
#SBATCH --job-name=zagreus
#SBATCH --output=zagreus_node53_20_cores.out
#SBATCH --ntasks=40
#SBATCH --threads-per-core=1
#SBATCH --ntasks-per-core=1
#SBATCH --mem-per-cpu=2G
#SBATCH --partition=AVX
#SBATCH --nodelist=node53
#SBATCH --exclusive
CORE=20
echo "#AVX mode"
for j in {1..5}
do
        echo "#$j mode"
        for i in 500 1000 2000 5000
        do
                echo "#$i times"	
        	for k in $(seq 1 $CORE)
		do
                	./Zagreus/main 1 $i 16 $j &
                done
                wait
                echo "#Frecuency"
                lscpu | grep -e "CPU MHz:"
        done
done
echo "#AVX+VNNI mode"
for j in 8 16 32 64
do
        echo "#$j size"
        for k in {1..5}
        do
                echo "#$k mode"
                for i in 500 1000 2000 5000
                do
                        echo "#$i times"
                        for l in $(seq 1 $CORE)
                        do
                                ./Zagreus/main 2 $i $j $k &
                        done
                        wait
                        echo "#Frecuency"
                	lscpu | grep -e "CPU MHz:"
               done
        done
done
