#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <iterator>
#include <sstream>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */

    string line;
    vector<int> first, second;

    // Read line 1
    if (getline(std::cin, line))
    {
    istringstream iss(line);
    copy(istream_iterator<int>(iss), istream_iterator<int>(), back_inserter(first));
    }

    // Read line 2
    if (std::getline(std::cin, line))
    {
    std::istringstream iss(line);
    std::copy(istream_iterator<int>(iss), istream_iterator<int>(), back_inserter(second));
    }
    
    int n,m;
    if(first.size() == 2) {
        n = first.back();
        first.pop_back();
        m = first.back();
        first.pop_back();
    }

    cout << n << " " << m << endl;

    while(next_permutation(second.begin, second.begin+m))
    return 0;
}