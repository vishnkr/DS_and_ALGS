#include<iostream>
#include<cmath>

using namespace std;

bool isPalindrome(int x){
    if(x<0 || (x%10==0 && x!=0)){
        return false;
    }
    int reverse_num = 0;
    while(x>reverse_num){
        reverse_num = (reverse_num*10)+(x%10);
        x = floor(x/10);
    }
    return bool((x==reverse_num) || x==floor(reverse_num/10));
}

int main(){
    std::cout.setf(std::ios::boolalpha);
    cout << isPalindrome(5)<< isPalindrome(121) << isPalindrome(-121)<< isPalindrome(10) << endl;
    return 0;
}