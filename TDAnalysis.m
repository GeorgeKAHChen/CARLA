clear;
Length = 10000;
InteSize = 501;
IntervalMin = 0;
IntervalMax = 2;
x = (1: Length);
y = (1: InteSize);
y = (y - 1) / (InteSize - 1);
y = y * (IntervalMax - IntervalMin) + IntervalMin;
[z, txt, raw] = xlsread('InputTable.xlsx');
x = double(x);
y = double(y);
mesh(y, x, z)