/*
Programmer: Ben Diegel
Program: Wage calculator
Date: 9/29/17
*/

#include<iostream>
using namespace std;

//prototpyes
int getHours(int refEmpId[], int refHours[]);
int getPayRate(int refEmpId[], double refPayRate[]);
int getWages(int refHours[], double refPayRate[], double refWages[]);
int displayWages(int refEmpId[], double refWages[]);

// global because it is constant. Size of the arrays
const int EMPLOYEES = 7;


int main(){
    // declared all my arrays in main to pass to the functions
    int empId[EMPLOYEES] = {5658845, 4520125, 7895122, 8777541, 8451277, 1302850, 7580489};
    int hours[EMPLOYEES] = {};
    double payRate[EMPLOYEES] = {};
    double wages[EMPLOYEES] = {};

    getHours(empId, hours); // gets the employee hours, passed id and hours array 
    getPayRate(empId, payRate); // gets the employee pay rate, passed id and payrate array
    getWages(hours, payRate, wages); // calculates the wages, passes hours, pay, and wages array
    displayWages(empId, wages); // this displays all wages, passed id and wages array

    return 0;
}

// asks the user for employees hours using thier id number
int getHours(int refEmpId[], int refHours[]){
    int i = 0; // counter

    for(i; i <= EMPLOYEES-1; i++){ 
        cout << "\nPlease enter the hours for employee: " << refEmpId[i] << "\n>>"; 
        cin >> refHours[i];
        while(refHours[i] < 0){ // input val to catch negatives
            cout << "Please enter positive values\n>>";
            cin >> refHours[i];
        }
    }
    return 0;
}

// asks the user for the emplyoees pay rate using their id number
int getPayRate(int refEmpId[], double refPayRate[]){
    int i = 0; // counter

    for(i; i <= EMPLOYEES-1; i++){
        cout <<"\nPlease enter the pay rate for employee: " << refEmpId[i] << "\n>>";
        cin >> refPayRate[i];
        while(refPayRate[i] < 15){ // to catch values less than 15 
            cout << "Please enter a value greater than 15\n>>";
            cin >> refPayRate[i];
        }
    }
    return 0;
}

// uses the employees hours and pay to calculate hours
int getWages(int refHours[], double refPayRate[], double refWages[]){
    int i = 0;

    for(i; i <= EMPLOYEES-1; i++){
        refWages[i] = refHours[i] * refPayRate[i];
    }
    return 0;
}

// diplays the emplyoees id number along with its pay rate 
int displayWages(int refEmpId[], double refWages[]){
    int i = 0;

    // tried to make a fancy box 
    for(i; i <= EMPLOYEES-1; i++){
        cout << "\n************************"
             << "\n*Employee: "<<refEmpId[i]<<"     *"
             << "\n*Wages: $"<<refWages[i]<<"            *"
             << "\n************************" << endl;

    }
    return 0;
}
