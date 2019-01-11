#include <iostream>
using namespace std;

string a,b,c;

int main()
{
    a="125999679";
    b="324777";

    for(int i=0;i<a.length();i++){
        if((int)a[i]>=(int)b[i]){
            c+=a[i];
        }else{
            c+=b[i];
        }
    }
    cout << c << endl;

}
