#include <iostream>
#include <vector>

using std::cerr;
using std::cout;
using std::endl;
using std::vector;

/*
void getFiles()
{
    ifstream file("rand100000.txt"); // Replace "numbers.txt" with your file name
    int num;

    if (file.is_open())
    {
        while (file >> num)
        {
            arr.push_back(num);
        }
        file.close();
    }
    else
    {
        cerr << "Error opening file!" << endl;
    }
}
*/

void insertionSortInCPP(int *arr, int size)
{
    vector<int> vec(arr, arr + size);
    long long comparisons = 0;
    int n = vec.size();

    if (n <= 1)
    {
        return;
    }

    for (int i = 1; i < n; ++i)
    {
        int key = vec[i];
        int j = i - 1;

        while (j >= 0 && key < vec[j])
        {
            comparisons++;
            vec[j + 1] = vec[j];
            j--;
        }

        vec[j + 1] = key;
    }

    cout << "Total Amount of Comparisons For Insertion Sort in CPP: " << comparisons << endl;
}

extern "C"
{
    /*
    void GetFiles()
    {
        getFiles();
    }
    */

    void InsertionSortInCPP(int *arr, int size)
    {
        insertionSortInCPP(arr, size);
    }
}