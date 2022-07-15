#include <stdio.h>
#include <iostream>

int main(int argc, char **argv)
{
    int F;
    std::cout << "This program determines whether or not an integer number is in the Fibonacci sequence.\n";
    std::cout << "What number do you want to check? Press Enter when ready.\n";
    std::cin >> F;
    
    // We are going to determine whether or not it is a number in the Fibonacci sequence.
    // Initialisation. Alter these to use Fibonacci sequences starting at different points.
    int a;
    a = 0;
    int b;
    b = 1;
    
    // If the user enters one of the two initial terms, no additional calculation is needed.
    if(( F == a )||( F == b )) {
        std::cout << "You entered " << F << ". The two initial terms are in the Fibonacci sequence by default.\n";
        return 0;
    }
    
    // Third variable to store the calculated number.
    int c;
    c = a + b;
    
    // While the calculated number in the sequence is less than the entered number, keep calculating the Fibonacci
    // sequence.
    while( c < F ) {
        a = b;
        b = c;
        c = a + b;
    }
    
    if( c == F ) {
        std::cout << "\n" << F << " is a part of this Fibonacci sequence.\n";
    } else {
        std::cout << "\n" << F << " is not a part of this Fibonacci sequence.\n";
    }
    
    return 0;
}
