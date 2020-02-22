#include<iostream>
#include <time.h>
#include <stdlib.h>
#include<windows.h>
using namespace std;

int main()
{
    //Get seed value
    unsigned seed = time(0);

    //Variables
    srand(seed);
    int count;
    int one;
    int two;
    int three;
    int four;
    int five;
    int six;

    //Generate random numbers
    for (count = 1; count >= 1; count++)
    {   Sleep(2000);
        one = rand() % 6 + 1;

        two = rand() % 6 + 1;
        three = rand() % 6 + 1;
        four = rand() % 6 + 1;
        five = rand() % 6 + 1;
        six = rand() % 6 + 1;
        cout<<one<<two<<three<<four<<five<<six<<endl;


        if (one == 1 && two == 2 && three == 3 && four == 4 && five == 5 && six == 6)
        {
        cout << one << "\n";
        cout << two << "\n";
        cout << three << "\n";
        cout << four << "\n";
        cout << five << "\n";
        cout << six << "\n";
            break;
        }


    }
    cout << endl;
    cout << "It took" << count << " rolls to roll 1, 2, 3, 4, 5 & 6." << endl;

    return 0;
}
