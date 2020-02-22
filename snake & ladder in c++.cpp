#include<iostream>
#include<stdlib.h>
#include<windows.h>
#include<stdbool.h>
#include<time.h>
using namespace std;
int dicetotal=0;
int dicetotal2 =0;
int matrix[10][10];
//unsigned seed = time(0);

//enum boolean { FALSE,TRUE };
void board()
{
    int i,j;
    for(i=0;i<10;i++)
      {for(j=0;j<10;j++)
         {
           matrix[i][j]=0;
        }
      }
 }
 void printmatrix()
 {
     int i,j;
  cout<<"\n";
          for(i=0;i<10;i++)
      {
          for(j=0;j<10;j++)
          {
              cout<<matrix[i][j]<<"\t";
          }
          cout<<"\n";
      }
 }
 void snakes()
 {
     if(dicetotal == 23 || dicetotal2 ==23)
     {
         cout<<"ohhh no  you got bitten by a snake"<<endl;
         Sleep(1000);
         if(dicetotal == 23)
         {
           dicetotal = 11;
          }
         else{
            dicetotal2 =11;
         }
    }
      if(dicetotal == 99 || dicetotal2 ==99)
     {
         cout<<"ohhh no  you got bitten by a snake"<<endl;
         Sleep(1000);
         if(dicetotal == 99)
         {
            dicetotal = 9;
         }
         else{
            dicetotal2 = 9;
         }
     }
      if(dicetotal == 79 || dicetotal2 ==79)
     {
         cout<<"ohhh no  you got bitten by a snake"<<endl;
         Sleep(1000);
         if(dicetotal == 79)
         {

         }
         dicetotal = 55;
     }
      if(dicetotal == 59 || dicetotal2 ==59)
     {
         cout<<"ohhh no  you got bitten by a snake"<<endl;
         if(dicetotal ==59)
         {
            Sleep(1000);
            dicetotal = 41;
         }
         else
         {
             Sleep(1000);
             dicetotal2 = 41;
         }
     }
      if(dicetotal == 21 || dicetotal2 ==21)
     {
         cout<<"ohhh no  you got bitten by a snake"<<endl;
         if(dicetotal == 21)
         {

            Sleep(1000);
            dicetotal = 5;
         }
         else
         {
             Sleep(1000);
             dicetotal2 =5;
         }
     }
 }
 void ladders()
 {
     if (dicetotal ==45 || dicetotal2 == 45)
     {   cout<<"yipeee u climbed a ladder"<<endl;
         if(dicetotal ==45)
         {

            Sleep(1000);
            dicetotal = 65;
         }
         else
         {
             Sleep(1000);
             dicetotal2 =65;
         }
     }
      if (dicetotal ==22 || dicetotal2 == 22)
     {   cout<<"yipeee u climbed a ladder"<<endl;
         if(dicetotal == 22)
         {

            Sleep(1000);
            dicetotal = 69;
         }
         else
         {
             Sleep(1000);
             dicetotal2 =69;
         }
     }
     if (dicetotal ==52 || dicetotal2 == 52)
     {   cout<<"yipeee u climbed a ladder"<<endl;
         if(dicetotal == 52)
         {

            Sleep(1000);
            dicetotal = 87;
         }
         else
         {
             Sleep(1000);
             dicetotal2 =87;
         }
     }
     if (dicetotal ==36 || dicetotal2 == 36)
     {   cout<<"yipeee u climbed a ladder"<<endl;
         if(dicetotal == 36)
         {

            Sleep(1000);
            dicetotal = 73;
         }
         else
         {
             Sleep(1000);
             dicetotal2 =73;
         }
     }
    if (dicetotal ==14 || dicetotal2 == 14)
     {   cout<<"yipeee u climbed a ladder"<<endl;
         if(dicetotal == 14)
         {
            Sleep(1000);
            dicetotal = 68;
         }
         else
         {
             Sleep(1000);
             dicetotal2 =68;
         }
     }
 }
void dicevalue()
{
    srand(time(0));
    int dice = 1+rand()%6;

    cout<<"dice ="<<dice<<endl;
    Sleep(2500);
    if (dicetotal==0 && dice ==6)
        {
            dicetotal= dice;
        }
    else if(dicetotal>0)
    {
        dicetotal=dicetotal + dice;
    }
     if(dicetotal > 100)
     {   Sleep(1000);
         dicetotal=dicetotal-dice;
     }
     ladders();
     snakes();
}
void dicevalue2()
{
    srand(time(0));
    int dice = 1+ rand()%6;

    cout<<"dice2 ="<<dice<<endl;
    Sleep(2000);
         if (dicetotal2==0 && dice ==6)
        {
            dicetotal2= dice;
        }
    else if(dicetotal2>0)
    {
        dicetotal2=dicetotal2 + dice;
    }
     if(dicetotal2 > 100)
     {   Sleep(1000);
         dicetotal2 = dicetotal2 - dice;
     }
    ladders();
    snakes();

}
void update()  // for returning values to the matrix
{
  if (dicetotal<11)
    matrix[0][dicetotal-1]=1;
  else if (dicetotal<21)
    matrix[1][dicetotal-11]=1;
    else if (dicetotal<31)
    matrix[2][dicetotal-21]=1;
    else if (dicetotal<41)
    matrix[3][dicetotal-31]=1;
    else if (dicetotal<51)
    matrix[4][dicetotal-41]=1;
    else if (dicetotal<61)
    matrix[5][dicetotal-51]=1;
    else if (dicetotal<71)
    matrix[6][dicetotal-61]=1;
    else if (dicetotal<81)
    matrix[7][dicetotal-71]=1;
    else if (dicetotal<91)
    matrix[8][dicetotal-81]=1;
    else if (dicetotal<=100)
    matrix[9][dicetotal-91]=1;
}
void update2()
{
    if (dicetotal2<11)
      matrix[0][dicetotal2-1]=2;
    else if (dicetotal2<21)
      matrix[1][dicetotal2-11]=2;
    else if (dicetotal2<31)
      matrix[2][dicetotal2-21]=2;
    else if (dicetotal2<41)
      matrix[3][dicetotal2-31]=2;
    else if (dicetotal2<51)
      matrix[4][dicetotal2-41]=2;
    else if (dicetotal2<61)
      matrix[5][dicetotal2-51]=2;
    else if (dicetotal2<71)
      matrix[6][dicetotal2-61]=2;
    else if (dicetotal2<81)
      matrix[7][dicetotal2-71]=2;
    else if (dicetotal2<91)
      matrix[8][dicetotal2-81]=2;
    else if (dicetotal2<=100)
      matrix[9][dicetotal2-91]=2;
}
int main()
{
   // enum boolean gameover;
    bool gameover = true;
    while(gameover == true)
    {
          board();
          dicevalue();
          update();
          dicevalue2();
          update2();
          printmatrix();
          if (dicetotal>=100)
          {
               cout<<"player 1 has won"<<endl;
               gameover = false;
          }
          else if (dicetotal2 >= 100)
           {
               cout<<"player 2 has won"<<endl;
               gameover = false;
           }

    }
    return 0;

}

