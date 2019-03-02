# BDA - Lab 01: Hadoop MapReduce in the cloud

Damien Rochat <damien.rochat@master.hes-so.ch>  
Dorian Magnin <dorian.magnin@master.hes-so.ch>  
Nelson Rocha <nelson.rocha@master.hes-so.ch>

## Task 2: Using Elastic MapReduce

#### EMR console summary

![](ex02/emr_console.png)

#### Max temperature chart

![](ex02/max_temperature_chart.png)

The overall highest recorded temperature is of 38.0 °C in 2003, year of the European heat wave.

#### EC2 instances

We used 3 m1.small instances (1 master and 2 cores).
For each one, the price of the on-demand EC2 is $0.044 + $0.011 for the EMR per hour.
Our cluster ran during 21 minutes.

The total cost is of `($0.055+$0.011)*3*0.35 = $0.0693`.

#### EMR job

From the job log file, the Mappers processed **2'831'380** input records (MAP_INPUT_RECORDS) and produced **2'821'078** records (MAP_OUTPUT_RECORDS).  
The Reducers processed **2'821'078** input records (REDUCE_INPUT_RECORDS) and produced **43** records (REDUCE_OUTPUT_RECORDS).
