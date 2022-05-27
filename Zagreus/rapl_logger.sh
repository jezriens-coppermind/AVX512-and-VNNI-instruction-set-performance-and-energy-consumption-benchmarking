#!/bin/bash

# RAPL-logger
# A tool to monitor the energy consumption of an application w/o root privileges
# It reads the RAPL registers located in the /sys/class folder at the frequency specified in line 41
# Usage: ./rapl_logger <your-app> <params-of-your-app>
# Author: Unai Lopez-Novoa, 2019
# License: MIT

#This function logs the RAPL readings from /sys/fs while app runs
function log_rapl_values()
{
  if [ "$PACKAGES" -eq 1 ]; then #Loop for 1 package, 2 readings

  while [ "1" ]; do
      cat /sys/class/powercap/intel-rapl/$RAPL_TAG_0/energy_uj >> /tmp/$TAG0_LOG
      cat /sys/class/powercap/intel-rapl/$RAPL_TAG_1/energy_uj >> /tmp/$TAG1_LOG
      sleep $FREQ
  done

  else #Loop for 2 packages, 4 readings

  while [ "1" ]; do
      cat /sys/class/powercap/intel-rapl/$RAPL_TAG_0/energy_uj >> /tmp/$TAG0_LOG
      cat /sys/class/powercap/intel-rapl/$RAPL_TAG_1/energy_uj >> /tmp/$TAG1_LOG

      cat /sys/class/powercap/intel-rapl/$RAPL_TAG_2/energy_uj >> /tmp/$TAG2_LOG
      cat /sys/class/powercap/intel-rapl/$RAPL_TAG_3/energy_uj >> /tmp/$TAG3_LOG

      sleep $FREQ
  done

  fi
}

# This function will calculate the Joules for each RAPL tag
# Arguments: Logfile path, RAPL TAG
function compute_energy_consumption()
{
    PREVIOUS=`head /tmp/$1 -n 1`
    OVERFLOWS=0

    while read line; do 
        CURRENT=$line; 
        if [ "$CURRENT" -lt "$PREVIOUS" ]; then
 	    OVERFLOWS=$(($OVERFLOWS+1)) 
        fi 
        PREVIOUS=$CURRENT
    done < "/tmp/$1"

    MAX_CORE_READ=`cat /sys/class/powercap/intel-rapl/$2/max_energy_range_uj`
    FIRST_READ=`head /tmp/$1 -n 1`
    LAST_READ=`tail /tmp/$1 -n 1`

    TOTAL_UJ=0
    if [ "$OVERFLOWS" -gt 0 ]; then
        TOTAL_UJ=$(((MAX_CORE_READ-FIRST_READ)+(MAX_CORE_READ*(OVERFLOWS-1))+(LAST_READ)))
    else
        TOTAL_UJ=$((LAST_READ-FIRST_READ))
    fi

    JOULES=`bc -l <<< $TOTAL_UJ/1000000`
    echo $JOULES
}

# CONFIGURE HERE RAPL-LOGGER
FREQ=0.1 #Seconds between each sample of RAPL registers
PACKAGES=1 #Number of sockets to be analysed. Currently 1 or 2 supported
REMOVE_LOGFILES=0 #1 = Yes, 0 = No; Remove logfiles after execution
RAPL_TAG_0=intel-rapl\:0
RAPL_TAG_1=intel-rapl\:0/intel-rapl\:0\:0
RAPL_TAG_2=intel-rapl\:1
RAPL_TAG_3=intel-rapl\:1/intel-rapl\:1\:0

#Check arguments
if [ "$#" -lt 1 ]; then
    echo "** RAPL-logger Error: You must provide the name of the app to profile"
    exit
fi

#Prepare logfiles
TIMESTAMP=`date +%s`
TAG0_LOG=rapllog+$TIMESTAMP+0
TAG1_LOG=rapllog+$TIMESTAMP+1
touch /tmp/$TAG0_LOG
touch /tmp/$TAG1_LOG

HZ=`bc -l <<< 1/$FREQ`

if [ "$PACKAGES" -eq 2 ]; then
    TAG2_LOG=rapllog+$TIMESTAMP+2
    TAG3_LOG=rapllog+$TIMESTAMP+3
    touch /tmp/$TAG2_LOG
    touch /tmp/$TAG3_LOG
    printf '** RAPL-logger - 2 packages - Sampling freq.  %4.1f Hz - Logfiles 0-3: /tmp/rapllog+%s\n' $HZ $TIMESTAMP
else
    printf '** RAPL-logger - 1 package - Sampling freq.  %4.1f Hz - Logfiles 0-1: /tmp/rapllog+%s\n' $HZ $TIMESTAMP
fi

#Initialise RAPL logs with first values, launch app and RAPL loggin routine
echo "** RAPL-logger - Profiling: ${@}"

cat /sys/class/powercap/intel-rapl/$RAPL_TAG_0/energy_uj >> /tmp/$TAG0_LOG
cat /sys/class/powercap/intel-rapl/$RAPL_TAG_1/energy_uj >> /tmp/$TAG1_LOG

if [ "$PACKAGES" -eq 2 ]; then
    cat /sys/class/powercap/intel-rapl/$RAPL_TAG_2/energy_uj >> /tmp/$TAG2_LOG
    cat /sys/class/powercap/intel-rapl/$RAPL_TAG_3/energy_uj >> /tmp/$TAG3_LOG
fi

TIME_START=`date +%s%3N`

eval "${@}" &
PROC_ID=$!

log_rapl_values &
disown
LOGGER_PID=$!


##Wait for app to end and terminate function logging RAPL values
wait $PROC_ID 
TIME_END=`date +%s%3N`
kill $LOGGER_PID

#Compute energy and avg. power consumption from logs

echo "** RAPL-logger - Process terminated, computing results"

TIME_DELTA=$((TIME_END-TIME_START))
TIME_SECONDS=`bc -l <<< $TIME_DELTA/1000`
printf "Recorded wall time (s): %8.4f\n" "$TIME_SECONDS"

TAG0_JOULES=$(compute_energy_consumption $TAG0_LOG $RAPL_TAG_0)
TAG0_WATTS=`bc -l <<< $TAG0_JOULES/$TIME_SECONDS`
TAG0_NAME=`cat /sys/class/powercap/intel-rapl/$RAPL_TAG_0/name`
printf "Domain $RAPL_TAG_0 ($TAG0_NAME) energy consumption (j): %8.4f\n" "$TAG0_JOULES"
printf "Domain $RAPL_TAG_0 ($TAG0_NAME) avg. power consumption (W): %8.4f\n" "$TAG0_WATTS"

TAG1_JOULES=$(compute_energy_consumption $TAG1_LOG $RAPL_TAG_1)
TAG1_WATTS=`bc -l <<< $TAG1_JOULES/$TIME_SECONDS`
TAG1_NAME=`cat /sys/class/powercap/intel-rapl/$RAPL_TAG_1/name`
printf "Domain $RAPL_TAG_1 ($TAG1_NAME) energy consumption (j): %8.4f\n" "$TAG1_JOULES"
printf "Domain $RAPL_TAG_1 ($TAG1_NAME) avg. power consumption (W): %8.4f\n" "$TAG1_WATTS"

if [ "$PACKAGES" -eq 2 ]; then #Print additional value for 2nd package

    TAG2_JOULES=$(compute_energy_consumption $TAG2_LOG $RAPL_TAG_2)
    TAG2_WATTS=`bc -l <<< $TAG2_JOULES/$TIME_SECONDS`
    TAG2_NAME=`cat /sys/class/powercap/intel-rapl/$RAPL_TAG_2/name`
    printf "Domain $RAPL_TAG_2 ($TAG2_NAME) energy consumption (j): %8.4f\n" "$TAG2_JOULES"
    printf "Domain $RAPL_TAG_2 ($TAG2_NAME) avg. power consumption (W): %8.4f\n" "$TAG2_WATTS"

    TAG3_JOULES=$(compute_energy_consumption $TAG3_LOG $RAPL_TAG_3)
    TAG3_WATTS=`bc -l <<< $TAG3_JOULES/$TIME_SECONDS`
    TAG3_NAME=`cat /sys/class/powercap/intel-rapl/$RAPL_TAG_3/name`
    printf "Domain $RAPL_TAG_3 ($TAG3_NAME) energy consumption (j): %8.4f\n" "$TAG3_JOULES"
    printf "Domain $RAPL_TAG_3 ($TAG3_NAME) avg. power consumption (W): %8.4f\n" "$TAG3_WATTS"

fi

#Remove logfiles if necessary
if [ "$REMOVE_LOGFILES" -eq 1 ]; then
    rm /tmp/$TAG0_LOG
    rm /tmp/$TAG1_LOG
    if [ "$PACKAGES" -eq 2 ]; then
        rm /tmp/$TAG2_LOG
        rm /tmp/$TAG3_LOG
    fi
fi