/**
 *author:Abu Jafar Shiddik
 *created:21-05-2023(17:51:05)
 **/
#include <bits/stdc++.h>
using namespace std;
/*
1:3
2:3
3:1
10:4
*/
vector<int> topKFrequent(vector<int> &nums, int k)
{
    map<int, int> mp;
    for (auto i : nums)
        mp[nums[i]]++;
    for (auto a : mp)
    {
        cout << a.first << ":" << a.second << "\n";
    }
}

// int main()
// {
//     vector<int> nums = {1, 1, 1, 2, 2, 2, 3, 10, 10, 10, 10};
//     int k;
//     cin >> k;
//     topKFrequent(nums, k);
//     for (int i = 0; i < nums.size(); i++)
//         // cout << nums[i] << " ";
//         return 0;
// }

int main() {
    std::vector<int> numbers = {1, 2, 2, 3, 3, 4, 4, 4, 4};
    std::map<int, int> frequencyMap;

    // Counting frequencies using a map
    for (const auto& number : numbers) {
        frequencyMap[number]++;
    }

    // Printing the frequency array
    for (const auto& pair : frequencyMap) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}