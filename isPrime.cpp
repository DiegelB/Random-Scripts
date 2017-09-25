/*
Programmer: Ben Diegel
Program: Prime number checker
Date: 9/23/17
*/
#include<fstream>
#include<iostream>

using namespace std;

//prototypes
bool isPrime(int num);

int main(){
    int num;

    // opening the file and getting it ready to write
    ofstream writeFile;
    writeFile.open("Prime_Num.txt");

    // loops between 1-100
    for(num = 0; num < 100; num++){
        if(isPrime(num)){ // sends each number to test if it is prime or not. If it is, then it writes to file
            writeFile << num << endl;
        }
    }
    writeFile.close();
    return 0;
}

bool isPrime(int num){
    if(num % 2 == 0 || num % 5 == 0){ // test to see if the number is divisible by 2 or 5 (meaning not prime)
        return false;
    }
    else{ // if it has no dividing factors, the number authenticates to true
        return true;
    }
}
