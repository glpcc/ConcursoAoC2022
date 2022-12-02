#include <iostream>

using namespace std;

int main(){
    char first_letter;
    char second_letter;
    int total_value; 
    int loose_values[3] = {3,1,2};
    int win_values[3] = {2,3,1};
    while (cin >> first_letter)
    {
        cin >> second_letter;
        if (second_letter == 'X'){
            total_value += loose_values[first_letter - 'A'];
        }else if(second_letter == 'Y'){
            total_value += 3 + (first_letter - 'A') + 1;
        }else{
            total_value += 6 + win_values[first_letter-'A'];
        }
    }
    cout << total_value << '\n';
    return 0;
}