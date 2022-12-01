// read input.txt and add up each line. If there is an empty line append a 0

#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <sstream>
using namespace std;

int main()
{
    ifstream in("input.txt");
    string line;
    std::list<int> listOfInts;
    listOfInts.push_back(0);
    while (getline(in, line))
    {
        if (line.empty())
        {
            listOfInts.push_back(0);
        }
        else
        {
            listOfInts.back() += stoi(line);
        }
    }

    // print max value in list
    cout << *max_element(listOfInts.begin(), listOfInts.end()) << endl;

    // print sum of the three largest values in list
    listOfInts.sort();
    listOfInts.reverse();
    int sum = 0;
    for (int i = 0; i < 3; i++)
    {
        sum += listOfInts.front();
        listOfInts.pop_front();
    }
    cout << sum << endl;

    return 0;
}