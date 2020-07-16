/*
 * Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
 */

#include <iostream>

int gauss(int n){
    return n * (n + 1) / 2;
}


int divideGauss(int n, int f){
    return f * gauss(n / f);
}


int answer() {
    int n = 999;
    return divideGauss(n, 3) + divideGauss(n, 5) + divideGauss(n,15);
}


int main() {
    std::cout << "Answer: " << answer() << std::endl;
    return 0;
}
