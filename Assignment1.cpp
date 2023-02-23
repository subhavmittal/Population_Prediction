#include<iostream>
using namespace std;
class LagrangePolynomial{
    private:
        int n;
        int *x;
        float *fx1;
        float *fx2;
        long double *a1;
        long double *a2;
    public:
        LagrangePolynomial(int n);
        void load_data(float x1[][2], float x2[][2]);
        void generate_polynomial();
        long double* evaluate_polynomial(long double x);
};
LagrangePolynomial::LagrangePolynomial(int n){
    this->n = n;
    x = new int[n];
    fx1 = new float[n];
    fx2 = new float[n];
    a1 = new long double[n];
    a2 = new long double[n];
}
void LagrangePolynomial::load_data(float x1[][2], float x2[][2]){
    for(int i=0; i<n; i++){
        this->x[(n-1) - i] = x1[i][0];
        this->fx1[i] = x1[i][1];
        this->fx2[i] = x2[i][1];
    }
}
void LagrangePolynomial::generate_polynomial(){
    long double **F1 = new long double*[n];
    long double **F2 = new long double*[n];
    for(int i=0; i<n; i++){
        F1[i] = new long double[i+1];
        F2[i] = new long double[i+1];
    }
    for(int i=0; i<n; i++){
        F1[i][0] = fx1[i];
        F2[i][0] = fx2[i];
    }
    for (int i=1; i<n; i++){
        for (int j=1; j<=i; j++){
            F1[i][j] = (F1[i][j-1] - F1[i-1][j-1])/(x[(n-1)-i] - x[(n-1)-(i-j)]);
            F2[i][j] = (F2[i][j-1] - F2[i-1][j-1])/(x[(n-1)-i] - x[(n-1)-(i-j)]);
        }
    }
    for(int i=0; i<n; i++){
        a1[(n-1)-i] = F1[i][i];
        a2[(n-1)-i] = F2[i][i];
    }
}
long double* LagrangePolynomial::evaluate_polynomial(long double x){
    long double val_1 = a1[0];
    long double der_1 = val_1;
    long double val_2 = a2[0];
    long double der_2 = val_2;
    for (int i=1; i<n-1; i++){
        val_1 = val_1*(x - this->x[i]) + a1[i];
        der_1 = der_1*(x - this->x[i+1]) + val_1;
        val_2 = val_2*(x - this->x[i]) + a2[i];
        der_2 = der_2*(x - this->x[i+1]) + val_2;
    }
    val_1 = val_1*(x - this->x[n-1]) + a1[n-1];
    val_2 = val_2*(x - this->x[n-1]) + a2[n-1];
    long double der = der_1 - der_2;
    long double val = val_1 - val_2;
    long double *return_val = new long double[2];
    return_val[0] = val;
    return_val[1] = der;
    return return_val;
}
int main(){
    float x1[][2] = {{2000,1.28},{2005,1.31},{2010,1.35},{2015,1.39},{2023,1.41}};
    float x2[][2] = {{2000,1.04},{2005,1.1},{2010,1.2},{2015,1.32},{2023,1.40}};
    LagrangePolynomial lp(5);
    lp.load_data(x1, x2);
    lp.generate_polynomial();
    
    cout<<lp.evaluate_polynomial(2000)[0]<<" "<<lp.evaluate_polynomial(2000)[1]<<endl;
    cout<<lp.evaluate_polynomial(2005)[0]<<" "<<lp.evaluate_polynomial(2005)[1]<<endl;
    cout<<lp.evaluate_polynomial(2010)[0]<<" "<<lp.evaluate_polynomial(2010)[1]<<endl;
    cout<<lp.evaluate_polynomial(2015)[0]<<" "<<lp.evaluate_polynomial(2015)[1]<<endl;
    cout<<lp.evaluate_polynomial(2021.5234)[0]<<" "<<lp.evaluate_polynomial(2021.5234)[1]<<endl;
    return 0;
}