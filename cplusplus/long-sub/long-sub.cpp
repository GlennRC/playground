#include <iostream>
#include <string>

using namespace std; 
 
class Solution {
    
    public:
        int longestSubstring(string s) 
        {
            if(s.length() < 2)
                return s.length();

            int l = 0;
            string temp = "";
            for(int j=0;j<s.length();j++) 
            {
                if(l >= s.length()-j)
                    break;

                temp = s[j];
                for(int k=j+1;k<s.length();k++)
                {
                    // if temp does not contain the letter
                    if(temp.find(s[k]) == string::npos) 
                        temp = temp + s[k];
                    else
                        break;
                }
                if(temp.length() > l)
                    l = temp.length();
            }   
            return l;
        }

        int lengthOfLongestSubstring(string s) {
            int occuringIndex[128];
            
            for(int i = 0; i<128; i++){
                occuringIndex[i] = -1;
            }
            
            int record_start = 0;
            int startIndex = 0;
            int currentIndex = 0;
            int len = 0;
            for(auto i: s){
                // if character never been recorded
                if(occuringIndex[i] == -1){
                    // record the index
                    occuringIndex[i] = currentIndex;
                }else{
                    if(currentIndex-startIndex > len){
                        record_start = startIndex;
                        len = currentIndex - startIndex;
                    }
                    startIndex = (startIndex > occuringIndex[i]+1)? startIndex:occuringIndex[i]+1;
                    occuringIndex[i] = currentIndex;
                }
                currentIndex ++;
            }
            if(len < currentIndex - startIndex) len = currentIndex - startIndex;
            return len;
        }
};


int main()
{
    Solution sol;
    cout << sol.lengthOfLongestSubstring("apple");

    return 0;
}
