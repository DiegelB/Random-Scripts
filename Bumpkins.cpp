/*
Programmer: Ben Diegel
Program: Bumpkins of Bumpus
Date: 9/20/17
Notes: I had some trouble with this one. I got the general idea of how to read through the files 
and what i needed to do to get the warrented output. However, I couldnt get my program to fully 
work. I have a bug where my program wont write to file over 6 doorways, plus I couldnt
figure out how to number the doorways correctly without tearing apart all of my code and redoing it.
Also, i know i should have made this program more modular. But Im not too comfertable with
passing by reference with changing data plus having to write to file. Im sure I could have cleaned
up my code by doing so, but atleast i know there is room for improvment for myself.
*/
#include<iostream>
#include<fstream>
#include<string>

using namespace std;

// prototypes
int readFile();
string doorwayDecision(double heightOfBumpkin2, double heightOfDoor2, char bumpUnits2, char doorUnits2);

int main(){
    readFile();
    return 0;
}

int readFile(){
    int numberOfBumpkins, numberOfDoors, counter4Doors = 1, counter4Bumps = 1; //i have 2 counters for each loop
    double heightOfBumpkin, heightOfDoor;
    string bumpkinName;
    char bumpUnits, doorUnits; 

    //preps files for reading and writing
    ifstream readFile;
    ofstream writeFile;
    readFile.open("bumpkins.in");
    writeFile.open("bumpkins.out");

    // first reads the number of bumps to see how many times it must loop over the name, #doors, heigt, 
    // and unit boilerplates
    readFile >> numberOfBumpkins;

    // the first loop test to see if it has read all of the bumps
    while(counter4Bumps <= numberOfBumpkins){
        readFile >> bumpkinName;
        writeFile << bumpkinName << endl;

        readFile >> numberOfDoors
                 >> heightOfBumpkin >> bumpUnits;
        // second loop tests to read all the doors
        do {
            readFile >> heightOfDoor >> doorUnits;
            writeFile << "Doorway " << counter4Doors << ": " 
                      // sends all the info it reads to the decision funciton that returns the string
                      // to write to file
                      << doorwayDecision(heightOfBumpkin, heightOfDoor, bumpUnits, doorUnits) << endl;
            counter4Doors++;
        } while(counter4Doors <= numberOfDoors);
        counter4Bumps++;
    }
    
    // closing my files to avoid errors
    readFile.close();
    writeFile.close();
    return 0;
}

// function that decieds how the bumps need to traverse the doors
string doorwayDecision(double heightOfBumpkin2, double heightOfDoor2, char bumpUnits2, char doorUnits2){
    // ALL OF MY NUMBERS ARE CONVERTED TO CENTIMETERS
    // all of this converts the bump heights to centimeters
    if(bumpUnits2 == 'i'){
        heightOfBumpkin2 = heightOfBumpkin2 * 2.54;
    }
    else if(bumpUnits2 == 'f'){
        heightOfBumpkin2 = heightOfBumpkin2 * (12*2.54);
    }
    else if(bumpUnits2 == 'y'){
        heightOfBumpkin2 = heightOfBumpkin2 * (3*(12*2.54));
    }
    else if(bumpUnits2 == 'm'){
        heightOfBumpkin2 = heightOfBumpkin2 * 100;
    }
    else if (bumpUnits2 == 'c'){
        heightOfBumpkin2 = heightOfBumpkin2;
    }

    // this is the statment that converts the doors to centimeters
    if(doorUnits2 == 'i'){
        heightOfDoor2 = heightOfDoor2 * 2.54;
    }
    else if(doorUnits2 == 'f'){
        heightOfDoor2 = heightOfDoor2 * (12*2.54);
    }
    else if(doorUnits2 == 'y'){
        heightOfDoor2 = heightOfDoor2 * (3*(12*2.54));
    }
    else if(doorUnits2 == 'm'){
        heightOfDoor2 = heightOfDoor2 * 100;
    }
    else if (bumpUnits2 == 'c'){
        heightOfDoor2 = heightOfDoor2;
    }

    // this decition logic deciedes how the bumps need to traverse the doors and
    // returns that string
    if(heightOfDoor2 > heightOfBumpkin2 * 1.25){
        cout << heightOfDoor2 << endl << heightOfBumpkin2 << endl << "stils\n";
        return "Stilts";
    }
    else if(heightOfBumpkin2 * 1.25 >= heightOfDoor2 && heightOfDoor2 > heightOfBumpkin2 *1.05){
        cout << heightOfDoor2 << endl << heightOfBumpkin2 << endl << "walk\n";
        return "Walk";
    }
    else if(heightOfBumpkin2 * 1.05 >= heightOfDoor2 && heightOfDoor2 > heightOfBumpkin2 * 0.65){
        cout << heightOfDoor2 << endl << heightOfBumpkin2 << endl << "duck\n";
        return "Duck";
    }
    else if(heightOfBumpkin2 * 0.65 >= heightOfDoor2 && heightOfDoor2 > heightOfBumpkin2 * 0.40){
        cout << heightOfDoor2 << endl << heightOfBumpkin2 << endl << "crawl\n";
        return "Crawl";
    }
    else if(heightOfBumpkin2 * 0.40 >= heightOfDoor2 && heightOfDoor2 > heightOfBumpkin2 * 0.25){
        cout << heightOfDoor2 << endl << heightOfBumpkin2 << endl << "limbo\n";
        return "Limbo";
    }
    else if(heightOfBumpkin2 * 0.25 >= heightOfDoor2){
        cout << heightOfDoor2 << endl << heightOfBumpkin2 << endl << "blocked\n";
        return "Blocked";
    }
}
