import matplotlib.pyplot as plt
import numpy as np
import sys
import os

def main(node, number):
    filename = "zagreus_node" + str(node) + "_" + str(number) + "_cores.out"
    if not os.path.exists("Node"+str(node)):
        os.mkdir("Node"+str(node))
    if not os.path.exists("Node"+str(node)+"/res"):
        os.mkdir("Node"+str(node)+"/res")
    if not os.path.exists("Node"+str(node)+"/out"):
        os.mkdir("Node"+str(node)+"/out")
    resfile =  "Node"+str(node)+ "/res" + "/zagreus_node" + str(node) + "_" + str(number) + "_cores.res"

    mode = 1
    sumatory = 0
    lines = 0
    minimun = 100000000
    maximun = 0

    frec_num = 0

    frec_min_avx = 100000000
    frec_max_avx = 0
    frec_count_avx = 0
    frec_summatory_avx = 0

    frec_min_size8 = 100000000
    frec_max_size8 = 0
    frec_count_size8 = 0
    frec_summatory_size8 = 0

    frec_min_size16 = 100000000
    frec_max_size16 = 0
    frec_count_size16 = 0
    frec_summatory_size16 = 0

    frec_min_size32 = 100000000
    frec_max_size32 = 0
    frec_count_size32 = 0
    frec_summatory_size32 = 0

    frec_min_size64 = 100000000
    frec_max_size64 = 0
    frec_count_size64 = 0
    frec_summatory_size64 = 0

    energy_num = 0

    energy_min_avx = 100000000
    energy_max_avx = 0
    energy_count_avx = 0
    energy_summatory_avx = 0

    energy_min_size8 = 100000000
    energy_max_size8 = 0
    energy_count_size8 = 0
    energy_summatory_size8 = 0

    energy_min_size16 = 100000000
    energy_max_size16 = 0
    energy_count_size16 = 0
    energy_summatory_size16 = 0

    energy_min_size32 = 100000000
    energy_max_size32 = 0
    energy_count_size32 = 0
    energy_summatory_size32 = 0

    energy_min_size64 = 100000000
    energy_max_size64 = 0
    energy_count_size64 = 0
    energy_summatory_size64 = 0

    energy_min_mode1 = 100000000
    energy_max_mode1 = 0
    energy_count_mode1 = 0
    energy_summatory_mode1 = 0

    energy_min_mode2 = 100000000
    energy_max_mode2 = 0
    energy_count_mode2 = 0
    energy_summatory_mode2 = 0

    energy_min_mode3 = 100000000
    energy_max_mode3 = 0
    energy_count_mode3 = 0
    energy_summatory_mode3 = 0

    energy_min_mode4 = 100000000
    energy_max_mode4 = 0
    energy_count_mode4 = 0
    energy_summatory_mode4 = 0

    energy_min_mode5 = 100000000
    energy_max_mode5 = 0
    energy_count_mode5 = 0
    energy_summatory_mode5 = 0

    power_num = 0

    power_min_avx = 100000000
    power_max_avx = 0
    power_count_avx = 0
    power_summatory_avx = 0

    power_min_size8 = 100000000
    power_max_size8 = 0
    power_count_size8 = 0
    power_summatory_size8 = 0

    power_min_size16 = 100000000
    power_max_size16 = 0
    power_count_size16 = 0
    power_summatory_size16 = 0

    power_min_size32 = 100000000
    power_max_size32 = 0
    power_count_size32 = 0
    power_summatory_size32 = 0

    power_min_size64 = 100000000
    power_max_size64 = 0
    power_count_size64 = 0
    power_summatory_size64 = 0
    
    power_min_mode1 = 100000000
    power_max_mode1 = 0
    power_count_mode1 = 0
    power_summatory_mode1 = 0

    power_min_mode2 = 100000000
    power_max_mode2 = 0
    power_count_mode2 = 0
    power_summatory_mode2 = 0

    power_min_mode3 = 100000000
    power_max_mode3 = 0
    power_count_mode3 = 0
    power_summatory_mode3 = 0

    power_min_mode4 = 100000000
    power_max_mode4 = 0
    power_count_mode4 = 0
    power_summatory_mode4 = 0

    power_min_mode5 = 100000000
    power_max_mode5 = 0
    power_count_mode5 = 0
    power_summatory_mode5 = 0

    res = open(resfile, "w")
    file = open(filename, "r")

    res.write("**************************")
    res.write("\n* Executed on Node: " + str(node))
    res.write("\n* Executed with " + str(number) + " cores\n")
    res.write("**************************")

    for line in file:
        if line.startswith("#"):
            if line.startswith("#1 mode"):
                mode = 1
                frec_num+=1
                energy_num+=1
                power_num+=1
                res.write("\n\n\n(500M) Min Max Avg (1000M) Min Max Avg (2000M) Min Max Avg (5000M) Min Max Avg\n")

            elif line.startswith("#2 mode"):
                mode = 2
                res.write("\n")

            elif line.startswith("#3 mode"):
                mode = 3
                res.write("\n")

            elif line.startswith("#4 mode"):
                mode = 4
                res.write("\n")

            elif line.startswith("#5 mode"):
                mode = 5
                res.write("\n")

            
        elif line.startswith("CPU"):
            res.write("Mode" + str(mode) + "," + str(minimun) + "," + str(maximun) + "," + str("{:.2f},".format(sumatory/lines)))

            sumatory = 0
            lines = 0
            minimun = 100000000
            maximun = 0

            if frec_num == 1:  
                frec = float(line.split(":")[1].rstrip(" "))
                if frec < frec_min_avx:
                    frec_min_avx = frec
                if frec > frec_max_avx:
                    frec_max_avx = frec
                frec_count_avx+=1
                frec_summatory_avx+=frec
            elif frec_num == 2:
                frec = float(line.split(":")[1].rstrip(" "))
                if frec < frec_min_size8:
                    frec_min_size8 = frec
                if frec > frec_max_size8:
                    frec_max_size8 = frec
                frec_count_size8+=1
                frec_summatory_size8+=frec
            elif frec_num == 3:
                frec = float(line.split(":")[1].rstrip(" "))
                if frec < frec_min_size16:
                    frec_min_size16 = frec
                if frec > frec_max_size16:
                    frec_max_size16 = frec
                frec_count_size16+=1
                frec_summatory_size16+=frec
            elif frec_num == 4:
                frec = float(line.split(":")[1].rstrip(" "))
                if frec < frec_min_size32:
                    frec_min_size32 = frec
                if frec > frec_max_size32:
                    frec_max_size32 = frec
                frec_count_size32+=1
                frec_summatory_size32+=frec
            elif frec_num == 5:
                frec = float(line.split(":")[1].rstrip(" "))
                if frec < frec_min_size64:
                    frec_min_size64 = frec
                if frec > frec_max_size64:
                    frec_max_size64 = frec
                frec_count_size64+=1
                frec_summatory_size64+=frec
        
        elif line.startswith("/"):
            pass

        elif line.startswith("** "):
            pass

        elif line.startswith("Recorded"):
            pass

        elif line.startswith("Executing the following command:"):
            pass

        elif not line.rstrip():
            pass

        elif line.startswith("Domain intel-rapl:0/intel-rapl:0:0"):
            pass
            
        elif line.startswith("Domain intel-rapl:0 (package-0) energy consumption (j):"):
            energy = float(line.split(":")[2])/1000
            if energy_num == 1:  
                if energy < energy_min_avx:
                    energy_min_avx = energy
                if energy > energy_max_avx:
                    energy_max_avx = energy
                energy_count_avx+=1
                energy_summatory_avx+=energy

            elif energy_num == 2:
                if energy < energy_min_size8:
                    energy_min_size8 = energy
                if energy > energy_max_size8:
                    energy_max_size8 = energy
                energy_count_size8+=1
                energy_summatory_size8+=energy

            elif energy_num == 3:
                if energy < energy_min_size16:
                    energy_min_size16 = energy
                if energy > energy_max_size16:
                    energy_max_size16 = energy
                energy_count_size16+=1
                energy_summatory_size16+=energy

            elif energy_num == 4:
                if energy < energy_min_size32:
                    energy_min_size32 = energy
                if energy > energy_max_size32:
                    energy_max_size32 = energy
                energy_count_size32+=1
                energy_summatory_size32+=energy

            elif energy_num == 5:
                if energy < energy_min_size64:
                    energy_min_size64 = energy
                if energy > energy_max_size64:
                    energy_max_size64 = energy
                energy_count_size64+=1
                energy_summatory_size64+=energy

            if mode == 1 and energy_num > 1:
                if energy < energy_min_mode1:
                    energy_min_mode1 = energy
                if energy > energy_max_mode1:
                    energy_max_mode1 = energy
                energy_count_mode1+=1
                energy_summatory_mode1+=energy

            elif mode == 2:
                if energy < energy_min_mode2:
                    energy_min_mode2 = energy
                if energy > energy_max_mode2:
                    energy_max_mode2 = energy
                energy_count_mode2+=1
                energy_summatory_mode2+=energy

            elif mode == 3:
                if energy < energy_min_mode3:
                    energy_min_mode3 = energy
                if energy > energy_max_mode3:
                    energy_max_mode3 = energy
                energy_count_mode3+=1
                energy_summatory_mode3+=energy

            elif mode == 4:
                if energy < energy_min_mode4:
                    energy_min_mode4 = energy
                if energy > energy_max_mode4:
                    energy_max_mode4 = energy
                energy_count_mode4+=1
                energy_summatory_mode4+=energy

            elif mode == 5:
                if energy < energy_min_mode5:
                    energy_min_mode5 = energy
                if energy > energy_max_mode5:
                    energy_max_mode5 = energy
                energy_count_mode5+=1
                energy_summatory_mode5+=energy


        elif line.startswith("Domain intel-rapl:0 (package-0) avg. power consumption (W):"):
            power = float(line.split(":")[2])/1000
            if power_num == 1:  
                if power < power_min_avx:
                    power_min_avx = power
                if power > power_max_avx:
                    power_max_avx = power
                power_count_avx+=1
                power_summatory_avx+=power

            elif power_num == 2:
                if power < power_min_size8:
                    power_min_size8 = power
                if power > power_max_size8:
                    power_max_size8 = power
                power_count_size8+=1
                power_summatory_size8+=power

            elif power_num == 3:
                if power < power_min_size16:
                    power_min_size16 = power
                if power > power_max_size16:
                    power_max_size16 = power
                power_count_size16+=1
                power_summatory_size16+=power

            elif power_num == 4:
                if power < power_min_size32:
                    power_min_size32 = power
                if power > power_max_size32:
                    power_max_size32 = power
                power_count_size32+=1
                power_summatory_size32+=power
                
            elif power_num == 5:
                if power < power_min_size64:
                    power_min_size64 = power
                if power > power_max_size64:
                    power_max_size64 = power
                power_count_size64+=1
                power_summatory_size64+=power

            if mode == 1 and power_num > 1:
                if power < power_min_mode1:
                    power_min_mode1 = power
                if power > power_max_mode1:
                    power_max_mode1 = power
                power_count_mode1+=1
                power_summatory_mode1+=power

            elif mode == 2:
                if power < power_min_mode2:
                    power_min_mode2 = power
                if power > power_max_mode2:
                    power_max_mode2 = power
                power_count_mode2+=1
                power_summatory_mode2+=power

            elif mode == 3:
                if power < power_min_mode3:
                    power_min_mode3 = power
                if power > power_max_mode3:
                    power_max_mode3 = power
                power_count_mode3+=1
                power_summatory_mode3+=power

            elif mode == 4:
                if power < power_min_mode4:
                    power_min_mode4 = power
                if power > power_max_mode4:
                    power_max_mode4 = power
                power_count_mode4+=1
                power_summatory_mode4+=power

            elif mode == 5:
                if power < power_min_mode5:
                    power_min_mode5 = power
                if power > power_max_mode5:
                    power_max_mode5 = power
                power_count_mode5+=1
                power_summatory_mode5+=power

        else:
            number = float(line.split("s")[0])
            if number < minimun:
                minimun = number
            if number > maximun:
                maximun = number
            sumatory+=number
            lines+=1
    
    res.write("\n\n**************************\n")
    res.write("Frecuency During Test\n")
    res.write("\nMin frecuency avx: " + str(frec_min_avx)+" Hz")
    res.write("\nMax frecuency avx: " + str(frec_max_avx)+" Hz")
    res.write("\nAverage frecuency avx: " + str("{:.2f} Hz".format(frec_summatory_avx/frec_count_avx)))

    res.write("\nMin frecuency size8: " + str(frec_min_size8)+" Hz")
    res.write("\nMax frecuency size8: " + str(frec_max_size8)+" Hz")
    res.write("\nAverage frecuency size8: " + str("{:.2f} Hz".format(frec_summatory_size8/frec_count_size8)))

    res.write("\nMin frecuency size16: " + str(frec_min_size16)+" Hz")
    res.write("\nMax frecuency size16: " + str(frec_max_size16)+" Hz")
    res.write("\nAverage frecuency size16: " + str("{:.2f} Hz".format(frec_summatory_size16/frec_count_size16)))

    res.write("\nMin frecuency size32: " + str(frec_min_size32)+" Hz")
    res.write("\nMax frecuency size32: " + str(frec_max_size32)+" Hz")
    res.write("\nAverage frecuency size32: " + str("{:.2f} Hz".format(frec_summatory_size32/frec_count_size32)))

    res.write("\nMin frecuency size64: " + str(frec_min_size64)+" Hz")
    res.write("\nMax frecuency size64: " + str(frec_max_size64)+" Hz")
    res.write("\nAverage frecuency size64: " + str("{:.2f} Hz".format(frec_summatory_size64/frec_count_size64)))
    res.write("\n**************************\n")

    if energy_count_avx !=0 :

        res.write("\n\n**************************\n")
        res.write("Energy During Test\n")
        res.write("\nMin energy avx: " + str("{:.2f} kJ".format(energy_min_avx)))
        res.write("\nMax energy avx: " + str("{:.2f} kJ".format(energy_max_avx)))
        res.write("\nAverage energy avx: " + str("{:.2f} kJ".format(energy_summatory_avx/energy_count_avx)))

        res.write("\nMin energy size8: " + str("{:.2f} kJ".format(energy_min_size8)))
        res.write("\nMax energy size8: " + str("{:.2f} kJ".format(energy_max_size8)))
        res.write("\nAverage energy size8: " + str("{:.2f} kJ".format(energy_summatory_size8/energy_count_size8)))

        res.write("\nMin energy size16: " + str("{:.2f} kJ".format(energy_min_size16)))
        res.write("\nMax energy size16: " + str("{:.2f} kJ".format(energy_max_size16)))
        res.write("\nAverage energy size16: " + str("{:.2f} kJ".format(energy_summatory_size16/energy_count_size16)))

        res.write("\nMin energy size32: " + str("{:.2f} kJ".format(energy_min_size32)))
        res.write("\nMax energy size32: " + str("{:.2f} kJ".format(energy_max_size32)))
        res.write("\nAverage energy size32: " + str("{:.2f} kJ".format(energy_summatory_size32/energy_count_size32)))

        res.write("\nMin energy size64: " + str("{:.2f} kJ".format(energy_min_size64)))
        res.write("\nMax energy size64: " + str("{:.2f} kJ".format(energy_max_size64)))
        res.write("\nAverage energy size64: " + str("{:.2f} kJ".format(energy_summatory_size64/energy_count_size64)))

        res.write("\nMin energy mode1: " + str("{:.2f} kJ".format(energy_min_mode1)))
        res.write("\nMax energy mode1: " + str("{:.2f} kJ".format(energy_max_mode1)))
        res.write("\nAverage energy mode1: " + str("{:.2f} kJ".format(energy_summatory_mode1/energy_count_mode1)))

        res.write("\nMin energy mode2: " + str("{:.2f} kJ".format(energy_min_mode2)))
        res.write("\nMax energy mode2: " + str("{:.2f} kJ".format(energy_max_mode2)))
        res.write("\nAverage energy mode2: " + str("{:.2f} kJ".format(energy_summatory_mode2/energy_count_mode2)))

        res.write("\nMin energy mode3: " + str("{:.2f} kJ".format(energy_min_mode3)))
        res.write("\nMax energy mode3: " + str("{:.2f} kJ".format(energy_max_mode3)))
        res.write("\nAverage energy mode3: " + str("{:.2f} kJ".format(energy_summatory_mode3/energy_count_mode3)))

        res.write("\nMin energy mode4: " + str("{:.2f} kJ".format(energy_min_mode4)))
        res.write("\nMax energy mode4: " + str("{:.2f} kJ".format(energy_max_mode4)))
        res.write("\nAverage energy mode4: " + str("{:.2f} kJ".format(energy_summatory_mode4/energy_count_mode4)))

        res.write("\nMin energy mode5: " + str("{:.2f} kJ".format(energy_min_mode5)))
        res.write("\nMax energy mode5: " + str("{:.2f} kJ".format(energy_max_mode5)))
        res.write("\nAverage energy mode5: " + str("{:.2f} kJ".format(energy_summatory_mode5/energy_count_mode5)))
        res.write("\n**************************\n")

        res.write("\n\n**************************\n")
        res.write("Power During Test\n")
        res.write("\nMin power avx: " + str("{:.2f} kJ".format(power_min_avx)))
        res.write("\nMax power avx: " + str("{:.2f} kJ".format(power_max_avx)))
        res.write("\nAverage power avx: " + str("{:.2f} kJ".format(power_summatory_avx/power_count_avx)))

        res.write("\nMin power size8: " + str("{:.2f} kJ".format(power_min_size8)))
        res.write("\nMax power size8: " + str("{:.2f} kJ".format(power_max_size8)))
        res.write("\nAverage power size8: " + str("{:.2f} kJ".format(power_summatory_size8/power_count_size8)))

        res.write("\nMin power size16: " + str("{:.2f} kJ".format(power_min_size16)))
        res.write("\nMax power size16: " + str("{:.2f} kJ".format(power_max_size16)))
        res.write("\nAverage power size16: " + str("{:.2f} kJ".format(power_summatory_size16/power_count_size16)))

        res.write("\nMin power size32: " + str("{:.2f} kJ".format(power_min_size32)))
        res.write("\nMax power size32: " + str("{:.2f} kJ".format(power_max_size32)))
        res.write("\nAverage power size32: " + str("{:.2f} kJ".format(power_summatory_size32/power_count_size32)))

        res.write("\nMin power size64: " + str("{:.2f} kJ".format(power_min_size64)))
        res.write("\nMax power size64: " + str("{:.2f} kJ".format(power_max_size64)))
        res.write("\nAverage power size64: " + str("{:.2f} kJ".format(power_summatory_size64/power_count_size64)))

        res.write("\nMin power mode1: " + str("{:.2f} kJ".format(power_min_mode1)))
        res.write("\nMax power mode1: " + str("{:.2f} kJ".format(power_max_mode1)))
        res.write("\nAverage power mode1: " + str("{:.2f} kJ".format(power_summatory_mode1/power_count_mode1)))

        res.write("\nMin power mode2: " + str("{:.2f} kJ".format(power_min_mode2)))
        res.write("\nMax power mode2: " + str("{:.2f} kJ".format(power_max_mode2)))
        res.write("\nAverage power mode2: " + str("{:.2f} kJ".format(power_summatory_mode2/power_count_mode2)))

        res.write("\nMin power mode3: " + str("{:.2f} kJ".format(power_min_mode3)))
        res.write("\nMax power mode3: " + str("{:.2f} kJ".format(power_max_mode3)))
        res.write("\nAverage power mode3: " + str("{:.2f} kJ".format(power_summatory_mode3/power_count_mode3)))

        res.write("\nMin power mode4: " + str("{:.2f} kJ".format(power_min_mode4)))
        res.write("\nMax power mode4: " + str("{:.2f} kJ".format(power_max_mode4)))
        res.write("\nAverage power mode4: " + str("{:.2f} kJ".format(power_summatory_mode4/power_count_mode4)))

        res.write("\nMin power mode5: " + str("{:.2f} kJ".format(power_min_mode5)))
        res.write("\nMax power mode5: " + str("{:.2f} kJ".format(power_max_mode5)))
        res.write("\nAverage power mode5: " + str("{:.2f} kJ".format(power_summatory_mode5/power_count_mode5)))
        res.write("\n**************************\n")

    file.close()
    res.close()

    os.replace(filename, "Node"+str(node)+"/out/"+filename)

def generate_charts(node):
    os.chdir("Node" + str(node))
    if not os.path.exists("charts"):
        os.mkdir("charts")
    if not os.path.exists("charts/avx512"):
        os.mkdir("charts/avx512")
    if not os.path.exists("charts/vnni"):
        os.mkdir("charts/vnni")
    if not os.path.exists("charts/vnni/size8"):
        os.mkdir("charts/vnni/size8")
    if not os.path.exists("charts/vnni/size16"):
        os.mkdir("charts/vnni/size16")
    if not os.path.exists("charts/vnni/size32"):
        os.mkdir("charts/vnni/size32")
    if not os.path.exists("charts/vnni/size64"):
        os.mkdir("charts/vnni/size64")
    if not os.path.exists("charts/frecuency"):
        os.mkdir("charts/frecuency")

    #Exectution Time Get AVX512
    for i in range(1,6):    
        generate_chart_avx(1, 2, 3, 500, i, node)
        generate_chart_avx(5, 6, 7, 1000, i, node)
        generate_chart_avx(9, 10, 11, 2000, i, node)
        generate_chart_avx(13, 14, 15, 5000, i, node)

    #Execution Time Get VNNI
    for j in [8, 16, 32, 64]:
        for i in range(1,6):    
            generate_chart_vnni(1, 2, 3, 500, i, j, node)
            generate_chart_vnni(5, 6, 7, 1000, i, j, node)
            generate_chart_vnni(9, 10, 11, 2000, i, j, node)
            generate_chart_vnni(13, 14, 15, 5000, i, j, node)

    #Chart Frequency AVX512
    generate_chart_frec(node)

    for i in [8, 16, 32, 64]:
        generate_chart_frec_vnni(node, i)

    generate_chart_ener(node)
    generate_chart_power(node)

    for i in [8, 16, 32, 64]:
        generate_chart_ener_vnni(node, i)
        generate_chart_power_vnni(node, i)

    for i in range(1, 6):
        generate_chart_power_vnni_mode(node, i)
        generate_chart_energy_vnni_mode(node, i)

def generate_chart_avx(x, y, z, times, mode, node):
    name = 'AVX512 ' + str(times) + ' Times - Mode ' + str(mode)
    minimun = []
    maximun = []
    average = []
    cores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for core in range(1, 21):
        line_num = 0
        file = open("res/zagreus_node" + str(node) + "_" + str(core) + "_cores.res", "r")
        for line in file:
            if line.startswith("Mode"+ str(mode)):
                if line_num == 0:
                    minimun.append(float(line.split(",")[x]))
                    maximun.append(float(line.split(",")[y]))
                    average.append(float(line.split(",")[z]))
                    line_num += 1
        file.close()

    coefficients = np.polyfit(cores, minimun, 2)
    poly = np.poly1d(coefficients)
    new_minimun = poly(cores)

    coefficients = np.polyfit(cores, maximun, 2)
    poly = np.poly1d(coefficients)
    new_maximun = poly(cores)
    
    coefficients = np.polyfit(cores, average, 2)
    poly = np.poly1d(coefficients)
    new_average = poly(cores)

    plt.plot(cores, minimun, color='green', linewidth=0.5, label='Row min')
    plt.plot(cores, new_minimun, color='green', linewidth=2, label='Poly min')
    plt.plot(cores, maximun, color='red', linewidth=0.5, label='Row max')
    plt.plot(cores, new_maximun, color='red', linewidth=2, label='Poly max')
    plt.plot(cores, average, color='blue', linewidth=0.5, label='Row avg')
    plt.plot(cores, new_average, color='blue', linewidth=2, label='Poly avg')

    plt.title(name, fontsize=14)
    plt.xlabel('Cores', fontsize=14)
    plt.ylabel('Tex (seconds)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.xticks(cores,cores)
    plt.savefig('charts/avx512/avx512_' + str(times) + 'M_mode_' + str(mode) + '.png')
    plt.close()

def generate_chart_vnni(x, y, z, times, mode, size, node):
    name = 'VNNI ' + str(size) + ' ' + str(times) + ' Times - Mode ' + str(mode)
    minimun = []
    maximun = []
    average = []
    cores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    if size == 8:
        wanted_line = 1
    elif size == 16:
        wanted_line = 2
    elif size == 32:
        wanted_line = 3
    elif size == 64:
        wanted_line = 4

    for core in range(1, 21):
        line_num = 0
        file = open("res/zagreus_node" + str(node) + "_" + str(core) + "_cores.res", "r")
        for line in file:
            if line.startswith("Mode"+ str(mode)):
                if line_num == wanted_line:
                    minimun.append(float(line.split(",")[x]))
                    maximun.append(float(line.split(",")[y]))
                    average.append(float(line.split(",")[z]))
                line_num += 1
        file.close()

    coefficients = np.polyfit(cores, minimun, 2)
    poly = np.poly1d(coefficients)
    new_minimun = poly(cores)

    coefficients = np.polyfit(cores, maximun, 2)
    poly = np.poly1d(coefficients)
    new_maximun = poly(cores)
    
    coefficients = np.polyfit(cores, average, 2)
    poly = np.poly1d(coefficients)
    new_average = poly(cores)

    plt.plot(cores, minimun, color='green', linewidth=0.5, label='Row min')
    plt.plot(cores, new_minimun, color='green', linewidth=2, label='Poly min')
    plt.plot(cores, maximun, color='red', linewidth=0.5, label='Row max')
    plt.plot(cores, new_maximun, color='red', linewidth=2, label='Poly max')
    plt.plot(cores, average, color='blue', linewidth=0.5, label='Row avg')
    plt.plot(cores, new_average, color='blue', linewidth=2, label='Poly avg')

    plt.title(name, fontsize=14)
    plt.xlabel('Cores', fontsize=14)
    plt.ylabel('Tex (seconds)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.xticks(cores,cores)
    plt.savefig('charts/vnni/size' + str(size) + '/vnni_size' + str(size) + '_' + str(times) + 'M_mode_' + str(mode) + '.png')
    plt.close()

def generate_chart_frec(node):
    name = 'Frecuency During Test - AVX512'
    minimun = []
    maximun = []
    average = []
    cores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for core in range(1, 21):
        file = open("res/zagreus_node" + str(node) + "_" + str(core) + "_cores.res", "r")
        for line in file:
            if line.startswith("Min frecuency avx: "):
                    minimun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Max frecuency avx: "):
                    maximun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Average frecuency avx: "):
                    average.append(int(line.split(": ")[1].split(".")[0]))
        file.close()

    coefficients = np.polyfit(cores, minimun, 2)
    poly = np.poly1d(coefficients)
    new_minimun = poly(cores)

    coefficients = np.polyfit(cores, maximun, 2)
    poly = np.poly1d(coefficients)
    new_maximun = poly(cores)
    
    coefficients = np.polyfit(cores, average, 2)
    poly = np.poly1d(coefficients)
    new_average = poly(cores)

    plt.plot(cores, minimun, color='green', linewidth=0.5, label='Row min')
    plt.plot(cores, new_minimun, color='green', linewidth=2, label='Poly min')
    plt.plot(cores, maximun, color='red', linewidth=0.5, label='Row max')
    plt.plot(cores, new_maximun, color='red', linewidth=2, label='Poly max')
    plt.plot(cores, average, color='blue', linewidth=0.5, label='Row avg')
    plt.plot(cores, new_average, color='blue', linewidth=2, label='Poly avg')

    plt.title(name, fontsize=14)
    plt.xlabel('Cores', fontsize=14)
    plt.ylabel('Frecuency (Hz)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.xticks(cores,cores)
    plt.savefig('charts/frecuency/frecuency_avx.png')
    plt.close()

def generate_chart_ener(node):
    name = 'Energy During Test - AVX512'
    minimun = []
    maximun = []
    average = []
    cores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for core in range(1, 21):
        file = open("res/zagreus_node" + str(node) + "_" + str(core) + "_cores.res", "r")
        for line in file:
            if line.startswith("Min energy avx: "):
                    minimun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Max energy avx: "):
                    maximun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Average energy avx: "):
                    average.append(int(line.split(": ")[1].split(".")[0]))
        file.close()

    coefficients = np.polyfit(cores, minimun, 2)
    poly = np.poly1d(coefficients)
    new_minimun = poly(cores)

    coefficients = np.polyfit(cores, maximun, 2)
    poly = np.poly1d(coefficients)
    new_maximun = poly(cores)
    
    coefficients = np.polyfit(cores, average, 2)
    poly = np.poly1d(coefficients)
    new_average = poly(cores)

    plt.plot(cores, minimun, color='green', linewidth=0.5, label='Row min')
    plt.plot(cores, new_minimun, color='green', linewidth=2, label='Poly min')
    plt.plot(cores, maximun, color='red', linewidth=0.5, label='Row max')
    plt.plot(cores, new_maximun, color='red', linewidth=2, label='Poly max')
    plt.plot(cores, average, color='blue', linewidth=0.5, label='Row avg')
    plt.plot(cores, new_average, color='blue', linewidth=2, label='Poly avg')

    plt.title(name, fontsize=14)
    plt.xlabel('Cores', fontsize=14)
    plt.ylabel('Energy (kJ)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.xticks(cores,cores)

    if not os.path.exists("charts/energy"):
        os.mkdir("charts/energy")

    plt.savefig('charts/energy/energy_avx.png')
    plt.close()

def generate_chart_power(node):
    name = 'Power During Test - AVX512'
    minimun = []
    maximun = []
    average = []
    cores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for core in range(1, 21):
        file = open("res/zagreus_node" + str(node) + "_" + str(core) + "_cores.res", "r")
        for line in file:
            if line.startswith("Min power avx: "):
                    minimun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Max power avx: "):
                    maximun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Average power avx: "):
                    average.append(int(line.split(": ")[1].split(".")[0]))
        file.close()

    coefficients = np.polyfit(cores, minimun, 2)
    poly = np.poly1d(coefficients)
    new_minimun = poly(cores)

    coefficients = np.polyfit(cores, maximun, 2)
    poly = np.poly1d(coefficients)
    new_maximun = poly(cores)
    
    coefficients = np.polyfit(cores, average, 2)
    poly = np.poly1d(coefficients)
    new_average = poly(cores)

    plt.plot(cores, minimun, color='green', linewidth=0.5, label='Row min')
    plt.plot(cores, new_minimun, color='green', linewidth=2, label='Poly min')
    plt.plot(cores, maximun, color='red', linewidth=0.5, label='Row max')
    plt.plot(cores, new_maximun, color='red', linewidth=2, label='Poly max')
    plt.plot(cores, average, color='blue', linewidth=0.5, label='Row avg')
    plt.plot(cores, new_average, color='blue', linewidth=2, label='Poly avg')

    plt.title(name, fontsize=14)
    plt.xlabel('Cores', fontsize=14)
    plt.ylabel('Power (kW)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.xticks(cores,cores)

    if not os.path.exists("charts/power"):
        os.mkdir("charts/power")

    plt.savefig('charts/power/power_avx.png')
    plt.close()

def generate_chart_frec_vnni(node, size):
    name = 'Frecuency During Test - VNNI ' + str(size)
    minimun = []
    maximun = []
    average = []
    cores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for core in range(1, 21):
        file = open("res/zagreus_node" + str(node) + "_" + str(core) + "_cores.res", "r")
        for line in file:
            if line.startswith("Min frecuency size" + str(size) +  ": "):
                    minimun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Max frecuency size" + str(size) +  ": "):
                    maximun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Average frecuency size" + str(size) +  ": "):
                    average.append(int(line.split(": ")[1].split(".")[0]))
        file.close()

    coefficients = np.polyfit(cores, minimun, 2)
    poly = np.poly1d(coefficients)
    new_minimun = poly(cores)

    coefficients = np.polyfit(cores, maximun, 2)
    poly = np.poly1d(coefficients)
    new_maximun = poly(cores)
    
    coefficients = np.polyfit(cores, average, 2)
    poly = np.poly1d(coefficients)
    new_average = poly(cores)

    plt.plot(cores, minimun, color='green', linewidth=0.5, label='Row min')
    plt.plot(cores, new_minimun, color='green', linewidth=2, label='Poly min')
    plt.plot(cores, maximun, color='red', linewidth=0.5, label='Row max')
    plt.plot(cores, new_maximun, color='red', linewidth=2, label='Poly max')
    plt.plot(cores, average, color='blue', linewidth=0.5, label='Row avg')
    plt.plot(cores, new_average, color='blue', linewidth=2, label='Poly avg')

    plt.title(name, fontsize=14)
    plt.xlabel('Cores', fontsize=14)
    plt.ylabel('Frecuency (Hz)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.xticks(cores,cores)
    plt.savefig('charts/frecuency/frecuency_size' + str(size) + '.png')
    plt.close()

def generate_chart_ener_vnni(node, size):
    name = 'Energy During Test - VNNI ' + str(size)
    minimun = []
    maximun = []
    average = []
    cores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for core in range(1, 21):
        file = open("res/zagreus_node" + str(node) + "_" + str(core) + "_cores.res", "r")
        for line in file:
            if line.startswith("Min energy size" + str(size) +  ": "):
                    minimun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Max energy size" + str(size) +  ": "):
                    maximun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Average energy size" + str(size) +  ": "):
                    average.append(int(line.split(": ")[1].split(".")[0]))
        file.close()

    coefficients = np.polyfit(cores, minimun, 2)
    poly = np.poly1d(coefficients)
    new_minimun = poly(cores)

    coefficients = np.polyfit(cores, maximun, 2)
    poly = np.poly1d(coefficients)
    new_maximun = poly(cores)
    
    coefficients = np.polyfit(cores, average, 2)
    poly = np.poly1d(coefficients)
    new_average = poly(cores)

    plt.plot(cores, minimun, color='green', linewidth=0.5, label='Row min')
    plt.plot(cores, new_minimun, color='green', linewidth=2, label='Poly min')
    plt.plot(cores, maximun, color='red', linewidth=0.5, label='Row max')
    plt.plot(cores, new_maximun, color='red', linewidth=2, label='Poly max')
    plt.plot(cores, average, color='blue', linewidth=0.5, label='Row avg')
    plt.plot(cores, new_average, color='blue', linewidth=2, label='Poly avg')

    plt.title(name, fontsize=14)
    plt.xlabel('Cores', fontsize=14)
    plt.ylabel('Energy (kJ)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.xticks(cores,cores)
    plt.savefig('charts/energy/energy_size' + str(size) + '.png')
    plt.close()

def generate_chart_power_vnni(node, size):
    name = 'Power During Test - VNNI ' + str(size)
    minimun = []
    maximun = []
    average = []
    cores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for core in range(1, 21):
        file = open("res/zagreus_node" + str(node) + "_" + str(core) + "_cores.res", "r")
        for line in file:
            if line.startswith("Min power size" + str(size) +  ": "):
                    minimun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Max power size" + str(size) +  ": "):
                    maximun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Average power size" + str(size) +  ": "):
                    average.append(int(line.split(": ")[1].split(".")[0]))
        file.close()

    coefficients = np.polyfit(cores, minimun, 2)
    poly = np.poly1d(coefficients)
    new_minimun = poly(cores)

    coefficients = np.polyfit(cores, maximun, 2)
    poly = np.poly1d(coefficients)
    new_maximun = poly(cores)
    
    coefficients = np.polyfit(cores, average, 2)
    poly = np.poly1d(coefficients)
    new_average = poly(cores)

    plt.plot(cores, minimun, color='green', linewidth=0.5, label='Row min')
    plt.plot(cores, new_minimun, color='green', linewidth=2, label='Poly min')
    plt.plot(cores, maximun, color='red', linewidth=0.5, label='Row max')
    plt.plot(cores, new_maximun, color='red', linewidth=2, label='Poly max')
    plt.plot(cores, average, color='blue', linewidth=0.5, label='Row avg')
    plt.plot(cores, new_average, color='blue', linewidth=2, label='Poly avg')

    plt.title(name, fontsize=14)
    plt.xlabel('Cores', fontsize=14)
    plt.ylabel('Power (kW)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.xticks(cores,cores)
    plt.savefig('charts/power/power_size' + str(size) + '.png')
    plt.close()

def generate_chart_power_vnni_mode(node, mode):
    name = 'Power During Test - VNNI | mode' + str(mode)
    minimun = []
    maximun = []
    average = []
    cores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for core in range(1, 21):
        file = open("res/zagreus_node" + str(node) + "_" + str(core) + "_cores.res", "r")
        for line in file:
            if line.startswith("Min power mode" + str(mode) +  ": "):
                    minimun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Max power mode" + str(mode) +  ": "):
                    maximun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Average power mode" + str(mode) +  ": "):
                    average.append(int(line.split(": ")[1].split(".")[0]))
        file.close()

    coefficients = np.polyfit(cores, minimun, 2)
    poly = np.poly1d(coefficients)
    new_minimun = poly(cores)

    coefficients = np.polyfit(cores, maximun, 2)
    poly = np.poly1d(coefficients)
    new_maximun = poly(cores)
    
    coefficients = np.polyfit(cores, average, 2)
    poly = np.poly1d(coefficients)
    new_average = poly(cores)

    plt.plot(cores, minimun, color='green', linewidth=0.5, label='Row min')
    plt.plot(cores, new_minimun, color='green', linewidth=2, label='Poly min')
    plt.plot(cores, maximun, color='red', linewidth=0.5, label='Row max')
    plt.plot(cores, new_maximun, color='red', linewidth=2, label='Poly max')
    plt.plot(cores, average, color='blue', linewidth=0.5, label='Row avg')
    plt.plot(cores, new_average, color='blue', linewidth=2, label='Poly avg')

    plt.title(name, fontsize=14)
    plt.xlabel('Cores', fontsize=14)
    plt.ylabel('Power (kW)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.xticks(cores,cores)
    plt.savefig('charts/power/power_mode' + str(mode) + '.png')
    plt.close()

def generate_chart_energy_vnni_mode(node, mode):
    name = 'Energy During Test - VNNI | mode' + str(mode)
    minimun = []
    maximun = []
    average = []
    cores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for core in range(1, 21):
        file = open("res/zagreus_node" + str(node) + "_" + str(core) + "_cores.res", "r")
        for line in file:
            if line.startswith("Min energy mode" + str(mode) +  ": "):
                    minimun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Max energy mode" + str(mode) +  ": "):
                    maximun.append(int(line.split(": ")[1].split(".")[0]))
            if line.startswith("Average energy mode" + str(mode) +  ": "):
                    average.append(int(line.split(": ")[1].split(".")[0]))
        file.close()

    coefficients = np.polyfit(cores, minimun, 2)
    poly = np.poly1d(coefficients)
    new_minimun = poly(cores)

    coefficients = np.polyfit(cores, maximun, 2)
    poly = np.poly1d(coefficients)
    new_maximun = poly(cores)
    
    coefficients = np.polyfit(cores, average, 2)
    poly = np.poly1d(coefficients)
    new_average = poly(cores)

    plt.plot(cores, minimun, color='green', linewidth=0.5, label='Row min')
    plt.plot(cores, new_minimun, color='green', linewidth=2, label='Poly min')
    plt.plot(cores, maximun, color='red', linewidth=0.5, label='Row max')
    plt.plot(cores, new_maximun, color='red', linewidth=2, label='Poly max')
    plt.plot(cores, average, color='blue', linewidth=0.5, label='Row avg')
    plt.plot(cores, new_average, color='blue', linewidth=2, label='Poly avg')

    plt.title(name, fontsize=14)
    plt.xlabel('Cores', fontsize=14)
    plt.ylabel('Energy (kJ)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.xticks(cores,cores)
    plt.savefig('charts/energy/energy_mode' + str(mode) + '.png')
    plt.close()

if __name__ == "__main__":
    for i in range(1, 21):
        main(53, i)

    generate_charts(53)