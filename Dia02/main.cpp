#include <iostream>

using namespace std;

int main(){
    char first_letter;
    char second_letter;
    int total_value; 
    while (cin >> first_letter)
    {
        cin >> second_letter;
        total_value += (second_letter - 'X') + 1;
        if ((second_letter == 'X' && first_letter == 'C') || (second_letter == 'Y' && first_letter == 'A') || (second_letter == 'Z' && first_letter == 'B')){
            total_value += 6;
        }else if(second_letter - 'X' == first_letter - 'A'){
            total_value += 3;
        }
    }
    cout << total_value << '\n';
    return 0;
}