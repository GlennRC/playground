#include <iostream>
#include <algorithm>    // std::sort
#include <vector>       // std::vector

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> nums3;
        nums3.reserve(nums1.size() + nums2.size());
        nums3.insert(nums3.end(), nums1.begin(), nums1.end());
        nums3.insert(nums3.end(), nums2.begin(), nums2.end());

        sort(nums3.begin(), nums3.end());        

        double median = 0;
        size_t size = nums3.size(); 
        double a = nums3[size / 2 - 1];
        double b = nums3[size / 2];
        if (size  % 2 == 0)
            median = (a + b) / 2;
        else 
            median = b;
      
        return median;
    }
};

int main() {

    Solution sol;
    vector<int> n1 = {1,2};
    vector<int> n2 = {3,4};
    cout << sol.findMedianSortedArrays(n1, n2);
    return 0;
}
