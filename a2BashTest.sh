#!/bin/bash
echo TEST 1:
cat ../tests/in01.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out01.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen

echo TEST 2:
cat ../tests/in02.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out02.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen

echo TEST 3:
cat ../tests/in03.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out03.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen

echo TEST 4:
cat ../tests/in04.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out04.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen

echo TEST 5:
cat ../tests/in05.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out05.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen

echo TEST 6:
cat ../tests/in06.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out06.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen

echo TEST 7:
cat ../tests/in07.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out07.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen



echo TEST 8:
cat ../tests/in08.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out08.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen



echo TEST 9:
cat ../tests/in09.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out09.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen


echo TEST 10:
cat ../tests/in10.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out10.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen

echo TEST 11:
cat ../tests/in11.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out11.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen

echo TEST 12:
cat ../tests/in12.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out12.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen

echo TEST 13:
cat ../tests/in13.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out13.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen

echo TEST 14:
cat ../tests/in14.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out14.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen

echo TEST 15:
cat ../tests/in15.txt | ./kwic2.py >  output.txt
MYVAR=$(diff ../tests/out15.txt output.txt)
chrlen=${#MYVAR}
echo $chrlen
