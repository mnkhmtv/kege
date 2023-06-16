# include<iostream>
# include<vector>
# include<fstream>
using namespace std;

int main(){
    int k = 21;
    int n = 300;
    ifstream f("/home/diana/ЕГЭ/Джобс 02.06/27_A_8962.txt");
    f >> n;
    vector<int> arr(n);

    for (int i = 0; i < n; i++) f >> arr[i];

    long mx = 0;
    for (int i = 0; i < n; i++){
        for (int j = i + k; j < n; j++){
            if (mx < (arr[j] + arr[i])){
                mx = arr[j] + arr[i];
            }
        }
    }
    int mx = 0;
    cout << mx << endl;
   
}
    // int k = 1000001;
    // int n = 4500000;