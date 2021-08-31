#include <iostream>
#include <fstream>
#include <cmath>

#define SIG_LENGTH 320
using namespace std;

extern double InputSignal_f32_1kHz_15kHz[SIG_LENGTH];
double RunningSumOuput[SIG_LENGTH];
double FirstDifferenceOutput[SIG_LENGTH];


void calc_running_sum(double *sig_src_arr, double *sig_dest_arr, int sig_length);
void calc_first_difference(double *sig_src_arr, double *sig_dest_arr, int sig_length);

int main()
{
    ofstream file1,file2,file3;

        calc_running_sum((double *)&InputSignal_f32_1kHz_15kHz[0], (double *)&RunningSumOuput[0], (int )SIG_LENGTH);
        calc_first_difference((double *)&InputSignal_f32_1kHz_15kHz[0], (double *)&FirstDifferenceOutput[0], (int )SIG_LENGTH);

        file1.open("running_sum_signal.dat");
        file2.open("first_diff_signal.dat");
        file3.open("input_signal.dat");

    for(int i =0 ;i<SIG_LENGTH;i++){
        file1<<RunningSumOuput[i]<<endl;
        file2<<FirstDifferenceOutput[i]<<endl;
        file3<<InputSignal_f32_1kHz_15kHz[i]<<endl;

    }

    file1.close();
    file2.close();
    file3.close();

    return 0;
}


void calc_running_sum(double *sig_src_arr, double *sig_dest_arr, int sig_length)
{
     for(int i = 0; i<sig_length;i++)
     {

         sig_dest_arr[i] = sig_dest_arr[i-1]+ sig_src_arr[i];
     }

}

void calc_first_difference(double *sig_src_arr, double *sig_dest_arr, int sig_length)
{
       for(int i = 0;i<sig_length;i++)
       {

           sig_dest_arr[i] =  sig_src_arr[i]-sig_src_arr[i-1];
       }

}
