#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;


int main(){

    string x, T;
    getline(cin, x);
    stringstream S(x);

    // start day, then days in month
    string nums[2];
    int numbers[2];
    for (int i = 0; i < 2; i ++){
        getline(S, T, ' ');
        nums[i] = T;
        stringstream tonum(nums[i]);
        tonum >> numbers[i];
    }

    cout << "Sun Mon Tue Wed Thr Fri Sat\n";

    //have numbers up till days in month
    //new row every 7
    int pee;

    for (int i = -numbers[0]+2; i < numbers[1]+1; i ++){
        if (pee % 7 == 0){
            cout << "\n";
        }
        if (i > 0){
            cout << i << "  ";
        }else{
            cout << ' ' << "  ";
        }
        pee ++;

    }
 


    return 0;

}







