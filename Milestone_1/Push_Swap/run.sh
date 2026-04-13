#!/usr/bin/env fish

set COUNT 10
set FLAGS "--adaptive"
set BENCH

for arg in $argv
    switch $arg
        case --bench
            set BENCH --bench
        case --simple --medium --complex --adaptive
            set FLAGS $FLAGS $arg
        case '*'
            set COUNT $arg
    end
end

set ARG (shuf -i 0-2147483647 -n $COUNT)
make -C (dirname (status filename))
./push_swap $FLAGS $BENCH $ARG