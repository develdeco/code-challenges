// Found in GeeksForGeeks
//#include <stdio.h>
using namespace std;

string countSort(string arr){
    int abc[26] = {0};
    int ord_a = int('a');
    for(int i=0;i<arr.length();i++){
        abc[int(arr[i])-ord_a]++;
    }
    string res = "";
    for(int i=0;i<26;i++){
        res += string(abc[i], char(ord_a+i));
    }
    return res;
}